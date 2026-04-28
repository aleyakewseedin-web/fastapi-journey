1. What is the difference between a Pod and a Deployment? Why would you use a Deployment instead of a bare Pod?
2. Why is a ConfigMap used for the MongoDB URL instead of hardcoding it in the Deployment YAML?
3. What happened to the original Pod when you scaled the WebApp to 3 replicas? Did it get replaced, or were new Pods added alongside it?
4. What would happen to the application if the MongoDB Pod crashed? How would Kubernetes respond?
5. What is one thing that surprised you or that you found confusing? How did you resolve it?

1) pod is abstraction of container deployment is abstraction of pods; we first create the deployment teh decide how many pods replicas we want 
2) ConfigMap is used for storing external URLS and is then connected to pod (it is for configurations).Deployment is mainly used for running pods,replicas,comtainers . hardcoding it in yaml would mean that if a crash happens in db yaml must be rebuilt and redployed
3) new pods were added alongside it
4) it will temporarily stop . kubernetes will rebuild a pod with new endpoint
5) nothing was very surprising it was as the video showed and explained  regarding deplyments ,services, pods.