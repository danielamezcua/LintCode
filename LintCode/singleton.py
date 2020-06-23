import threading

class Solution:
    _lock = threading.Lock()
    _instance = None
    # @return: The same instance of this class every time
    
    @classmethod
    def getInstance(cls):
        #check if instance is not set (maybe other thread is setting the instance)
        if Solution._instance == None:
            #acquire the lock to set the instance
            with _lock:
                #check if the instance is still not set
                if Solution._instance == None:
                    Solution._instance = Solution()

        return Solution._instance
