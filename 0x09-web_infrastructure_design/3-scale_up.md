## Scale up

### For every additional element, why you are adding it

1. We add one server and one balancer
2. Adding the server allow us to separate each component (web server, Application server, Database MYSQL) in their own server and having one server with all components to serve as a backup if any of the components or server fails.
3. Each server is being monitored and has a firewall
4. We added also an extra load balancer that will assist in handling more traffic across the whole infrastructure
