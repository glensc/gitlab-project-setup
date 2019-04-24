# Gitlab System Hook to configure new projects

Problem: only [a few][2] settings are configurable when new project is created. While the project has many more [settings to configure][1].

[1]: https://docs.gitlab.com/ce/user/project/settings/
[2]: https://gitlab.com/gitlab-org/omnibus-gitlab/blob/11.10.1+ce.0/files/gitlab-config-template/gitlab.rb.template#L65-71

## Install

```
docker-compose up -d
```

Create system hook from `/admin/hooks` from your GitLab instance:
- URL: `http://this-service:7888/`
- Trigger: `Repository update events`
