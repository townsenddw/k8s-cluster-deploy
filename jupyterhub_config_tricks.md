# Tricks for various requirements in JupyterHub

## Adding extra resources for specific users in a hub
```python
def add_resources(spawner, pod):
    users = ['List', 'of', 'users']
    if spawner.user.name in users:
    pod.spec.containers[0].resources.requests['memory'] = '4G'
    pod.spec.containers[0].resources.limits['memory'] = '4G'
    return pod
c.KubeSpawner.modify_pod_hook = add_resources
```