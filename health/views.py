import time
import asyncio
from dataclasses import asdict
from django.http import JsonResponse
from health_check import Database, Storage
from health_check.contrib.psutil import Disk
from health.decorators import health_check_timeout
from health.security import health_check_auth
from health.types import HealthStatus

START_TIME = time.time()

@health_check_auth
async def health_check_custom(request):
    database_check = Database()
    storage_check = Storage()
    disk_check = Disk()

    await database_check.get_result()
    await storage_check.get_result()

    check_results = await asyncio.gather(
        health_check_timeout(3)(database_check.get_result)(),
        health_check_timeout(5)(storage_check.get_result)(),
        health_check_timeout(0.5)(disk_check.get_result)(),
    )

    is_healthy = all(res.status == HealthStatus.HEALTHY for res in check_results)
    database_res, storage_res, disk_res = check_results

    uptime_sec = int(time.time() - START_TIME)
    uptime_str = f"{uptime_sec // 3600}:{(uptime_sec % 3600) // 60:02d}:{uptime_sec % 60:02d}"

    return JsonResponse({
        "status": HealthStatus.HEALTHY if is_healthy else HealthStatus.UNHEALTHY,
        "uptime": uptime_str,
        "checks": {
            "db": asdict(database_res),
            "storage": asdict(storage_res),
            "disk": asdict(disk_res),
        },
    })
