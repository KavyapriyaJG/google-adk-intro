# SESSIONS
1. **Maintain State**: 
    Store and access user data, preferences, and other information between interactions
2. **Track Conversation History**: 
    Automatically record and retrieve message history
3. **Personalize Responses**: 
    Use stored information to create more contextual and personalized agent experiences


# TYPES
1. InMemorySessionService (Built-in, refreshes on restart)
2. DatabaseSessionService (Any External DB for storage of convos)
3. VertexAISessionService (Google Cloud's AI platform)

This will:
1. Create a new session with user information
2. Initialize the agent with access to that session
3. Process a user query about the stored preferences
4. Display the agent's response based on the session data

## Key Components

### Session Service

The example uses the `InMemorySessionService` which stores sessions in memory:

```python
session_service = InMemorySessionService()
```

### Optional : Initial State

Sessions are created with an initial state containing user information:

```python
initial_state = {
    "user_name": "Tony Stark (Iron Man)",
    "user_preferences": """
        Enjoys inventing new technology and building advanced suits of armor.
        Loves shawarma and fine dining.
        Favorite TV show is anything with science or engineering.
        Enjoys witty banter and being the center of attention.
        Has a soft spot for helping others, even if he hides it behind sarcasm.
    """,
}
```

### Creating a Session

The example creates a session with a unique identifier:

```python
stateful_session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)
```

### Accessing State in Agent Instructions

The agent accesses session state using template variables in its instructions:

```python
instruction="""
You are a helpful assistant that answers questions about the user's preferences.

Here is some information about the user:
Name: 
{user_name}
Preferences: 
{user_preferences}
"""
```

# RUNNER
The Runner acts as the central coordinator for a single user invocation. 
Its responsibilities in the loop are:

**Initiation:**
Receives the end user's query (new_message) and typically appends it to the session history via the SessionService.

**Kick-off:**
Starts the event generation process by calling the main agent's execution method (e.g., agent_to_run.run_async(...)).

**Receive & Process:**
Waits for the agent logic to yield or emit an Event. Upon receiving an event, the Runner promptly processes it.

**Yield Upstream:**
Forwards the processed event onwards (e.g., to the calling application or UI for rendering).

**Iterate:**
Signals the agent logic that processing is complete for the yielded event, allowing it to resume and generate the next event.


### Running with Sessions

Sessions are integrated with the `Runner` to maintain state between interactions:

```python
runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service,
)
```