Unified Modeling Language

**Stereotype**
High level classification of an object, gives some idea as to what it is
# **UML Diagram Types**
**Structural Diagrams**
Composite structure diagram
Deployment diagram
Package diagram
Profile diagram
Class diagram
Object diagram
Component diagram

**Behavioral diagrams**
Activity diagram
Use case diagram
State machine diagram
Sequence diagram
Communication diagram
Interaction overview diagram 
Timing diagram

# **Class diagram**
If class is abstract, name is written in italics
Includes properties, methods and relations
\+ public
\-  private
\# protected
~ package local
For methods:
Parameters are marked as in, out, or inout

**Relations**

**Association** 
Connects classes. 
One to one: 1
One to many: 1..*
Many to many: *

**Inheritance**
Hollow arrow towards parent class

**Realization**
Dashed arrow towards the interface.
On top of the name of an interface is said \<\<Interface>>

**Dependency**
Dashed arrow towards the class which is depended upon.

**Aggregation**
When a class is part of a larger class
Continuous line with an unfilled diamond
Classes that form the aggregated one remain upon deletion

**Composition**
Classes that form it are deleted when the composite one is deleted
Continuous line with filled diamond



# **Component diagrams** 
Above the name says \<\<component>>
show how components are put together 
Illustrates architecture and dependencies
Class diagrams that focus on system components
Each component is responsible for one goal
On the right are Required interfaces (takes data from them)
On the left are Provided Interfaces (gives out data)
Port is a square at an edge. Used to expose interfaces.
Provided interface - complete circle on its end, line coming out of a port (lolipop)
Required interface - semicircle at the end
Subsystem classifier is a special type of a component classifier. Marked with subsystem

## **Relations**

**Association**
Semantic relationship between typed instances
Straight line

**Composition**
Strong form of aggregation. Requires a part instance to be included in at most one composite at a time
Parts are deleted with composite.
Filled diamond.

**Aggregation**
Child can exist on its own
Hollow diamond

**Constraint**
Condition or restriction explained in natural text or machine readable language.
Dashed line perpendicular to the main line with a note

**Dependency**
Dashed line with arrow

**Inheritance**
Hollow arrow near parent

# **Deployment diagram**
Illustrates the physical aspects
Illustrates the config of runtime processing nodes and the components that live on them
3D box = node, may be marked with stereotype notation
Connections represented by lines with optional stereotype notations

# **Object diagram**
Snapshot of a system at a specific point in time
Used for illustrating testing, for example
Modeling recursive relationships, looking at small parts of a system
Object: Class as name
attribute = value
Same links as classes

# **Package diagram**
Structural diagram that shows packages and dependencies between them
Location and organization of model elements
Rectangle with a smaller one on top left
If dependency with no stereotype, uses \<\<use>>
\<\<import>> - importing public as public
\<\<access>> - importing without making imported elements visible outside of the importing namespace
\<\<trace>> - historical development of one element into another
\<\<merge>> - metamodeling. Basically nonextistent.

# **Composite structure diagram**
Contains classes, interfaces, packages, and their relations. Representation of a software system or its part.
Shows internal parts of a class


# **Profile diagram**
Doman and platform-specific stereotypes
Stereotypes
Tags
KVPs of extra data under name (properties)
Restriction
String in closed brackets
Dashed arrow with \<\<apply>> applies a profile to a package

# **Use case diagram**
Defines the functional requirements of a system in terms of use cases
Model of intended functionality and its environment (actors)
Use cases only, no implementation detail
Actor is the one who interacts with a  system, depicted as a guy
\<\<extend>>
A use case can have extension points. They are implemented with a dashed arrow and \<\<extend>>
Valid password and Invalid password are extensions of a Login Account use case
\<\<include>>
When a use case includes another use case, such as placing an order including logging in
Generalization by use case is basically inheritance
Hollow arrow towards parent

Do it from the perspective of an actor, focus on what, not how, from a high level

# **Activities diagrams**
Illustration of workflows (basically BPMN)

# **State (machine) diagram**
Describing system behaviors in terms of a state machine
BPMN about states. Mainly applied to objects, but can be applied to pretty much anything.

4 types of events
Signal event
Call event
Time event
Change event


# **Sequence diagram**
Object interactions based on a time sequence
Object horizontally, time vertically
Async is an unfilled arrow
Return is a dashed arrow, so is create message
Focus of control is when an operation is being performed. Is a rectangle on a lifeline
Fragments
Alt 
Only one with a true condition can be executed
Opt
Executed only if condition is true
par
Parallel message processing
loop
loops
break
break.
Critical
Suspension of everything outside while this lasts
neg
message or event generated as a result of the inability to process another received message
assert
Group of messages to be executed after some condition was pre-checked
Strict
Strict Sequential message processing
(1 by 1 top to bottom)
Seq 
Non strict sequential message processing
(1 by 1 any order)
ignore
ignore whatever is after it
ref 
A reference to what is defined elsewhere
sd 
wraps the whole thing
# **Communications diagram**
Models dynamic behaviour of a system. focuses on object collaboration
Shows objects and messages the objects send between eachother

# **Interaction overview diagram**
Focuses on the flow of control
High level abstraction depicting activity between diagrams

# **Timing diagram**
Shows the behaviour of objects at a given time period
