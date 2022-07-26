'''
A Script for computing pairwise divergences in Prototypical Networks and Matching networks
Author: Jacó Gomes
'''

def pairwise_divergences(x: torch.Tensor,
                         y: torch.Tensor,
                         divergence: str) -> torch.Tensor:
    """
    # Arguments
        x: Query samples. A tensor of shape (n, d). n usually N_way * q_query, and d is the embeddings dimension.
        y: Class prototypes. A tensor of shape (N, d). N usually N_way, and d is the prototypes dimension.
        divergence: The desired divergence (string).
    Returns:
        A tensor of shape (q_queries * N_way, N_way).
    """  

    # Mahalanobis distance
    if divergence == 'mahalanobis':
        # Compute covariance matrix
        covariance = torch.cov(y.type(torch.float64).T)
        
        # Compute inverse of covariance matrix
        cov_Inv = torch.linalg.pinv(covariance).repeat(y.size(0),1,1) # add ".type(torch.float)" for cnielly's code

        x = x.unsqueeze(0)
        y = y.unsqueeze(1)
      
        n = x.size(1)
        m = y.size(1)
        d = x.size(2)
        N = y.size(0)
        assert d == y.size(2)

        x = x.unsqueeze(2).expand(N, n, m, d)
        y = y.unsqueeze(1).expand(N, n, m, d)

        # Compute Mahalanobis distances
        d = ((x-y).squeeze() @ cov_Inv @ torch.transpose((x-y).squeeze(), -2,-1))

        return torch.transpose(torch.diagonal(d, 0,1,2), -2, -1)  # add ".type(torch.double)" for oscarknagg's code


    # Kullback-Leibler divergence
    elif divergence == 'KL':
        x = x / torch.transpose((x.sum(1).expand(x.shape[1], x.shape[0])), 0, 1)
        y = y / torch.transpose((y.sum(1).expand(y.shape[1], y.shape[0])), 0, 1)
    
        n = x.size(0)
        m = y.size(0)
        d = x.size(1)
        assert d == y.size(1)

        x = x.unsqueeze(1).expand(n, m, d)
        y = y.unsqueeze(0).expand(n, m, d)

        # Since log (0) is negative infinity, let's add a small value to avoid it
        eps = 0.01

        return (x * torch.log((x+eps) / (y+eps))).sum(2) * 100


    # Itakura-Saito divergence
    elif divergence == 'IS':
        x = x / torch.transpose((x.sum(1).expand(x.shape[1], x.shape[0])), 0, 1)
        y = y / torch.transpose((y.sum(1).expand(y.shape[1], y.shape[0])), 0, 1)

        n = x.size(0)
        m = y.size(0)
        d = x.size(1)
        assert d == y.size(1)

        x = x.unsqueeze(1).expand(n, m, d)
        y = y.unsqueeze(0).expand(n, m, d)
        
        # Since log (0) is negative infinity, let's add a small value to avoid it
        eps = 0.01

        return (((x+eps) / (y+eps)) - torch.log((x+eps) / (y+eps)) - 1).sum(2)

    else:
        raise(ValueError('Unsupported similarity function'))
