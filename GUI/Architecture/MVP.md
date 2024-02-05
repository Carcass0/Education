Model - View - Presenter
- **Model:** Layer for storing data. It is responsible for handling the domain logic(real-world business rules) and communication with the database and network layers.
- **View:** UI(User Interface) layer. It provides the visualization of the data and keep a track of the user’s action in order to notify the Presenter.
- **Presenter:** Fetch the data from the model and applies the UI logic to decide what to display. It manages the state of the View and takes actions according to the user’s input notification from the View.

![[MVP.png]]

### Key Points of MVP Architecture

1. Communication between View-Presenter and Presenter-Model happens via an **interface(also called Contract)**.
2. One Presenter class manages one View at a time i.e., there is a one-to-one relationship between Presenter and View.
3. Model and View class doesn’t have knowledge about each other’s existence.

Allows to introduce more abstraction.
Basically a more decoupled version of [[MVC]].
More reusable and modular. 