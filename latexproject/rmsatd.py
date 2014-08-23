def rmsatd_precalc_bottleneck((sa, sb)):
    """Build RMSatd metric for structure A (`sa`) and B (`sb`).
    
    Each structure object has an `atoms` attribute, storing a
    list of atoms, whereas each atom has a `coords` attribute,
    storing a 1x3 numpy array with X,Y,Z coordinates.
    Furthermore, each structure has a `numpy_element_array`
    attribute, storing a 1xN numpy array encoding atom types as
    integer value, in order of the `atoms` list.
    
    References:
    http://stackoverflow.com/q/5954603/145400
    http://stackoverflow.com/a/1582742/145400
    http://stackoverflow.com/q/5480694/145400
    """
    # Pre-calculate Euclidean distance squares (all atoms in A
    # paired with all atoms in B).
    distmatrix_squared = scipy.spatial.distance.cdist(
        [a.coords for a in sa.atoms],
        [a.coords for a in sb.atoms],
        'sqeuclidean')
    # Transpose element type array of A (make column vector),
    # repeat n times to the right (n = number of atoms in B).
    Atypes2d = numpy.tile(
        sa.numpy_element_array[numpy.newaxis].T,
        (1, len(sb.atoms)))
    # Repeat element type array of structure B (row vector) to
    # the bottom (n = number of atoms in structure A).
    Btypes2d = numpy.tile(
        sb.numpy_element_array, (len(sa.atoms), 1))
    # Create bool matrix (True: non-matching type).
    type_matching_matrix = numpy.not_equal(Atypes2d, Btypes2d)
    # Overwrite distance values with NaN for non-matching types.
    distmatrix_squared[type_matching_matrix] = numpy.nan
    # Find minimal type-matching distance in each column, i.e.
    # for each atom in structure A.
    min_distances = bottleneck.nanmin(distmatrix_squared, axis=1)
    if not bottleneck.allnan(min_distances):
        # Return root mean of squares.
        return numpy.sqrt(bottleneck.nanmean(min_distances))
    # No match (impossible if A, B have equal configuration.)
    return None
    