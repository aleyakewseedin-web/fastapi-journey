1. What is the size of your image? Is it large or small — and why do you think that is?
2. How many layers does your image have? What does each major layer add?
3. What operating system and architecture does your image use? (from `docker inspect`)
4. **Image-specific question:**
   - 🏔️ Alpine: What happened when you installed `curl` inside the container? After you exited and restarted, was `curl` still installed? Why?
   - 🌐 Nginx: What does the port mapping `-p 8080:80` actually mean? What would happen if you used `-p 9090:80` instead?
   - 🐍 Python: What error did you get when trying `import requests`? What does this tell you about how Docker containers work?
   - 🐘 Postgres: Why did your data disappear after removing and recreating the container? What would you need to add to make it persist?
5. In one paragraph: what surprised you most about this lab?

Answers:
1-111MB copmared to other images in container its the smallest
2- 12 layers, each layer represents any modfications made to the layer below ... from bottom to top represents newest modifications
3- OS is LINUX and architecture is amd64
4-because container was destroyed so image is no longer there and must be pulled again
5-the differnt sizes of images that a container can hold it is not restricted to one size
