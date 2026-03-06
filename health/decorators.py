import asyncio
import time
from functools import wraps
from health_check.base import HealthCheckResult
from health.types import HealthStatus, CheckResult

def health_check_timeout(timeout=5):
    def decorator(check_func: HealthCheckResult):
        @wraps(check_func)
        async def _wrapped_check(*args, **kwargs) -> CheckResult:
            start_time = time.perf_counter()

            try:
                async with asyncio.timeout(timeout):
                    result: HealthCheckResult = await check_func(*args, **kwargs)
                    return CheckResult(
                        status=HealthStatus.HEALTHY if not result.error else HealthStatus.UNHEALTHY,
                        latency=result.time_taken,
                        error=result.error
                    )
            except TimeoutError:
                return CheckResult(
                    status=HealthStatus.TIMEOUT,
                    latency=timeout,
                )
            except Exception as e:
                return CheckResult(
                    status=HealthStatus.UNHEALTHY,
                    latency=round(time.perf_counter() - start_time, 3),
                    error=e
                )
        return _wrapped_check
    return decorator
