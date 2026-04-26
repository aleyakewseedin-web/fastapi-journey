Q&A1
What components do you see running in `kube-system`? Can you identify any components from the lecture (scheduler, etcd, api-server)?
answer:a scheduler,an api server,a controller manager,a proxy, a scheduler,2 coredns and one storage provisioner
Q&A 2
In the Events section of `kubectl describe`, what sequence of events happened before the pod started running? Which component scheduled the pod?
answer : first image was assigned to minikube (scheduled) and this was done by a default scheduler then was pulled by pod then container was created then started running
Q&A 3
After deleting the pod manually, did Kubernetes bring it back? Why or why not?

- What would need to be different (hint: think about what you'll learn in Lecture 4) for Kubernetes to automatically restart a deleted pod?

1. What is the difference between running a container with `docker run` and deploying a pod with `kubectl run`? Both used the same image — what changed?
2. In `kubectl describe pod`, what is the role of the **Scheduler** event? Which control plane component does that correspond to?
3. In `kubectl get pods -n kube-system`, name two components you recognised from the lecture and describe what they do.
4. Postgres: Why did the pod crash in Task 4 without environment variables? What does this tell you about how images communicate their requirements?
5. Task 6 reflection: After deleting the pod, Kubernetes did **not** restart it. In one paragraph, explain why, and what Kubernetes object would change this behaviour.

1) docker run runs container directly on docker and manages it while kubectl run will createa pod then container runs inside cluster which is managed :scheduled.. etc by kubernetes . what canged is that: environment and docker runs simple contai er ata time while kuberenetes system managing containers
2) it assigns pod to container, comamnd plane:kubectl shceduler
3) apiserver;it handles communications between cluster and eveyrything else
   scheduler; assigns pods to containers
4) because some images has requirements to run and this image earlier did not have its requirements satissfied .. in my case i firsly got an error but then i asked for help from chatgpt bcause i didnt understand why thats why my screenshit for task 4 is fixed and is not showung an error but then in task 5 i understood that its actually likely to happen. this tells that they have certain requirements that is stored in them and if not satissified they crash
5) because would change the pod was created as a standalone pod, meaning it was not managed by a "parent" controller. When deleting standalone pod, the cluster assumes its task is finished or no longer desired, as there is no underlying rule stating a specific number of copies must always exist. To change this behavior, you should use a Deployment
