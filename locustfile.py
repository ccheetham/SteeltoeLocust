from locust import HttpUser, task, between

class InitializrUser(HttpUser):

    wait_time = between(1, 2)

    @task
    def get_project(self):
        if 'steeltoe' in self.client.base_url:
            self.client.get('/api/project')
        elif 'spring' in self.client.base_url:
            self.client.get('/starter.zip')
        else:
            raise Exception("unknown URL: " + self.client.base_url)
