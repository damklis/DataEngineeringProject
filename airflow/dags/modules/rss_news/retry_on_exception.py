import functools
from log import log


@log
class RetryOnException:
    def __init__(self, retries):
        self._retries = retries

    def __call__(self, func):
        functools.update_wrapper(self, func)

        def wrapper(*args, **kwargs):
            while self._retries != 0:
                self.logger.info(f"Retries: {self._retries}")
                try:
                    func(*args, **kwargs)
                    self._retries = 0
                except Exception as err:
                    self.logger.info(f"Error occured: {err}")
                    self._retries -= 1
        return wrapper
