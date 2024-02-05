Model -View - Controller
- **Model:** This component stores the application data. It has no knowledge about the interface. The model is responsible for handling the domain logic(real-world business rules) and communication with the database and network layers.
- **View:** It is the UI(User Interface) layer that holds components that are visible on the screen. Moreover, it provides the visualization of the data stored in the Model and offers interaction to the user.
- **Controller:** This component establishes the relationship between the **View** and the **Model.** It contains the core application logic and gets informed of the user’s behavior and updates the Model as per the need.

![[MVC.png]]

Criticisms:
Too much coupling, like the view being coupled to the model, and controller being depended on a specific view
