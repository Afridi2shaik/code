from locust import task, run_single_user
from locust import FastHttpUser
import uuid
 
 
class load_test(FastHttpUser):
    host = "https://vip-loadtest-api.eizen.ai/analytics/v1"
 
    @task
    def t(self):
        with self.rest(
            "GET",
            "/user?email=keerthi%40eigenmaps.ai",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/user/list",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/tenant/2",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/tenant/2",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/source/analytics/4",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/model",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/raw-analytics/offline?tenantId=2&analyticsTypeId=2&analyticsId=4&zoneId=5&sourceId=6&interval=30&startTime=2024-04-11T00:15:24.958Z&endTime=2024-04-11T06:15:24.958Z",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/event?analyticIds=4&pageNumber=0&itemsPerPage=5&sourceId=6",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/analytics/tenant/2",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/analytics-type/tenant/2",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/source/analytics/4",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/model/4",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/source/41",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/tenant",
            headers={
                "Accept": "application/json",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "/zone",
            headers={
                "Accept": "application/json",
            },
            json={"name": str(uuid.uuid4()), "analyticsId": 1},
        ) as resp:
            pass
        with self.rest(
            "POST",
            "/source",
            headers={
                "Accept": "application/json",
            },
            json={
                "name": str(uuid.uuid4()),
                "userName": "string",
                "password": "string",
                "sourceUrl": "string",
                "description": "string",
                "sourceType": "string",
                "zoneId": 2,
                "models": [1, 2, 3],
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "/user",
            headers={
                "Accept": "application/json",
            },
            json={
                "userName": str(uuid.uuid4()),
                "email": str(uuid.uuid4()),
                "password": "string",
                "firstName": "string",
                "lastName": "string",
                "roles": ["user"],
                "tenantId": 1,
                "analyticsId": [1, 2],
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/user/5",
            headers={
                "Accept": "application/json",
            },
            json={
                "id": 5,
                "firstName": "Zuber",
                "lastName": "Abdul",
                "roles": ["User"],
                "analyticsId": [1, 2],
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/source/2",
            headers={
                "Accept": "application/json",
            },
            json={
                "name": "Hawk Headed Parrot feed Source",
                "userName": "Lset",
                "password": "Admin@123",
                "sourceUrl": "136.232.197.6:3037",
                "description": "Source camera for Hawk headed parrot feed",
                "sourceType": "camera",
                "models": [3],
            },
        ) as resp:
            pass
 
 
if __name__ == "__main__":
    run_single_user(load_test)
