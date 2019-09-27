class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # Quick return
        if x == z or y == z or x + y == z:
            return True

        # Find smaller and larger buckets
        if x <= y:
            smaller = x
            larger = y
        else:
            smaller = y
            larger = x
        
        z_smaller = 0
        z_larger = 0
        
        volume_set = set()
        
        while True:
            if z_smaller == 0:
                # Fill smaller to full
                z_smaller = smaller

                if z_smaller + z_larger == z:
                    return True

                volume_tuple = (z_smaller, z_larger)
                if volume_tuple in volume_set:
                    return False

                volume_set.add(volume_tuple)

            # Pour smaller into larger
            if z_larger + z_smaller <= larger:
                # Completely pour smaller into larger, smaller is now empty
                z_larger += z_smaller
                z_smaller = 0
            else:
                # Partially pour smaller into larger, larger is now full
                z_smaller -= (larger - z_larger)
                z_larger = larger

            if z_smaller + z_larger == z:
                return True

            volume_tuple = (z_smaller, z_larger)
            if volume_tuple in volume_set:
                return False

            volume_set.add(volume_tuple)

            # If larger is full
            if z_larger == larger:
                z_larger = 0

                if z_smaller + z_larger == z:
                    return True

                volume_tuple = (z_smaller, z_larger)
                if volume_tuple in volume_set:
                    return False

                volume_set.add(volume_tuple)