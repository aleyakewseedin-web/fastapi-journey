Just built a real-time polling app using FastAPI and WebSockets!
The idea was simple — create polls and vote on them. But the real challenge was making results update instantly across multiple browser tabs without any page refresh. That's what real-time means here: the moment someone votes, every connected tab sees the update immediately through a persistent WebSocket connection.
The backend handles two ways to vote. REST endpoints act as a fallback for when WebSocket isn't available. WebSockets handle the live experience — when a vote comes in, the server broadcasts it to every connected client instantly.
One challenge I ran into was opening the frontend via file:// in the browser, which blocked the WebSocket connection entirely. The fix was serving the HTML directly through a FastAPI endpoint (/index) , so everything runs over HTTP and the WebSocket connects properly.
The app is fully containerized with Docker and docker-compose, uses a .env file for sensitive config, and proves real-time behavior across 2+ open tabs simultaneously.


link to post : https://www.linkedin.com/posts/aleya-kewseedin-92349a3b1_fastapi-websockets-backenddevelopment-ugcPost-7457909367799967744-eWPq?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGShIasBxxlo6FrJrH_jj5Fr6GCAFdU9EWg