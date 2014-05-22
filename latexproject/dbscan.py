def dbscan(distmat, epsilon, minpoints):
    """Cluster objects via DBSCAN algorithm.
    
    Object pairwise distances are stored in `distmat`, which
    must be an N x N NumPy array for N objects.
    
    Return list containing one cluster label (int) per object.
    Label 0 corresponds to noise.
    """
    objs_indices = numpy.arange(distmat.shape[0])
    objs_clusterlabels = numpy.zeros(distmat.shape[0])
    objs_visited = numpy.zeros(distmat.shape[0]).astype(bool)

    distmask = (distmat > 0) & (distmat <= epsilon)
    neighbors = [distmask[i].nonzero()[0] for i in objs_indices]
    neighborhood_size = [len(n) for n in neighbors]

    # Iterate through objs in random order.
    numpy.random.shuffle(objs_indices)
    for neighbor_index_array in neighbors:
        numpy.random.shuffle(neighbor_index_array)

    clustercount = 0
    for objidx in objs_indices:
        if objs_visited[objidx]:
            continue
        objs_visited[objidx] = True
        if neighborhood_size[objidx] < minpoints:
            continue
        # The sample with current `objidx` is core point
        # of a new cluster. Label it with cluster 'id'.
        clustercount += 1
        objs_clusterlabels[objidx] = clustercount
        # Go through neighborhood of the identified core point.
        clustermember_indices = list(neighbors[objidx])
        for member_index in clustermember_indices:
            # If not in any cluster so far, add it to current:
            if not objs_clusterlabels[member_index]:
                objs_clusterlabels[member_index] = clustercount
            if objs_visited[member_index]:
                continue
            objs_visited[member_index] = True
            if neighborhood_size[objidx] < minpoints:
                continue
            # Object with current `member_index` is core point.
            # Add full neighborhood to `clustermember_indices`.
            clustermember_indices.extend(
                list(neighbors[member_index]))
    return objs_clusterlabels
