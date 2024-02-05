Model - View - Viewmodel
- **Model:** This layer is responsible for the abstraction of the data sources. Model and ViewModel work together to get and save the data.
- **View:** The purpose of this layer is to inform the ViewModel about the user’s action. This layer observes the ViewModel and does not contain any kind of application logic.
- **ViewModel:** It exposes those data streams which are relevant to the View. Moreover, it serves as a link between the Model and the View.

MVVM overcomes all drawbacks of [[MVC]] and [[MVP]] by clearly separating UI from the business logic.

![[MVVM.png]]
### Advantages of MVVM Architecture

- Enhance the reusability of code.
- All modules are independent which improves the testability of each layer.
- Makes project files maintainable and easy to make changes.

### Disadvantages of MVVM Architecture

- This design pattern is not ideal for small projects.
- If the data binding logic is too complex, the application debug will be a little harder.