# File config
```
/etc/gitlab-runner/config.toml - view via gitlab-ci-multi-runner list command
```
# Unregister runner
```
gitlab-ci-multi-runner unregister -n name|description
gitlab-runner unregister -n name|description
```

# Verify
If you remove runner on gitlab dashboard. You need to update from runner view.
```
gitlab-runner verify --delete
```

# List runner
```
gitlab-ci-multi-runner list
```

# Enable shared runner to a project
Settings > CI/CD Pipeline > Enable shared runner

# Building and cache space in shell runner
/home/gitlab-runner/builds (store code from project)
/home/gitlab-runner/cache (store cache)

# Building and cache space in docker runner (docker outside of docker)
/builds/<group>/<project-name>
/builds/<group>/<project-name>.tmp
/cache -> /var/lib/docker/volumes/<volid>/_data
