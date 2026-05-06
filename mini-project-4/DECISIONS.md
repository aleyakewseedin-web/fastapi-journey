
1. **Connection Management** — How does your connection manager track connected clients? What happens if a client disconnects mid-vote? Does your app handle this gracefully, or does it crash?

the class stores a list of connected webclients'with same poll ID in  a dictionary When a client connects to /ws/polls/{poll_id}, their WebSocket gets added to that list. When they disconnect, it gets removed via the disconnect() method.

If a client disconnects mid-vote, the WebSocketDisconnect exception is caught and the client is cleanly removed from the list — the app doesn't crash. There's also a dead connection inside broadcast() — if sending to a client fails, it gets removed silently.


2. **State Storage** — You are storing vote counts in memory. Why did you choose this over writing votes to a database? What breaks if you restart the server? What would need to change to make this production-ready?

In-memory was chosen because it's simple and fast for a mini project — no database setup needed. The tradeoff is that if you restart the server, all polls and votes are gone completely since nothing is saved to disk.
To make it production-ready you'd need a database like PostgreSQL or even Redis to persist the data, so restarts don't wipe everything.


3. **Concurrency** — What would happen if two users voted at exactly the same moment? Did you handle this in your implementation? If not, what is the risk?

Two users voting at the same moment could cause a race condition — both read the same count (e.g. 5), both add 1, and both write 6 instead of 7. This isn't handled in the current implementation. The risk is vote counts being slightly inaccurate under heavy simultaneous traffic. A fix would be using async locks or atomic database operations.

4. **REST vs WebSocket** — You now have two ways to vote: `POST /polls/{id}/vote` and the WebSocket. What is the key difference in behavior between them? When would a client prefer one over the other?

The key difference is that REST is a one-time request/response — you vote and get the updated poll back, but other tabs don't know about it unless they refresh. WebSocket is a persistent connection — when you vote, the server broadcasts the update to every connected client instantly.
You'd use REST as a fallback when WebSocket isn't available, or for server-to-server calls. You'd use WebSocket when you need every connected user to see updates in real time without any action on their end.