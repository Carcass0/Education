**OSI stands for Open Systems Interconnection**.
OSI model acts as a reference model and is not implemented on the Internet because of its late invention. The current model being used is the TCP/IP model.

![[OSI layers.png]]

The OSI model consists of seven abstraction layers arranged in a top-down order:
1. Physical Layer
2. Data Link Layer
3. Network Layer
4. Transport Layer
5. Session Layer
6. Presentation Layer
7. Application Layer

## **Physical Layer – Layer 1**
It is responsible for the actual physical connection between the devices. The physical layer contains information in the form of **bits.**
### Functions of the Physical Layer
- **Bit synchronization:** The physical layer provides the synchronization of the bits by providing a clock. This clock controls both sender and receiver thus providing synchronization at the bit level.
- **Bit rate control:** The Physical layer also defines the transmission rate i.e. the number of bits sent per second.
- **Physical topologies:** Physical layer specifies how the different, devices/nodes are arranged in a network i.e. bus, star, or mesh topology.
- **Transmission mode:** Physical layer also defines how the data flows between the two connected devices. The various transmission modes possible are Simplex, half-duplex and full-duplex.

## **Data Link Layer (DLL) – Layer 2**

The data link layer is responsible for the node-to-node delivery of the message. The main function of this layer is to make sure data transfer is error-free from one node to another, over the physical layer.
Divided into 
Logical Link Control ([[LLC]])
Media Access Control ([[MAC]])
### Functions of the Data Link Layer
- **Framing:** Framing is a function of the data link layer. It provides a way for a sender to transmit a set of bits that are meaningful to the receiver. This can be accomplished by attaching special bit patterns to the beginning and end of the frame.
- **Physical addressing:** After creating frames, the Data link layer adds physical addresses (MAC addresses) of the sender and/or receiver in the header of each frame.
- **Error control:** The data link layer provides the mechanism of error control in which it detects and retransmits damaged or lost frames.
- **Flow Control:** The data rate must be constant on both sides else the data may get corrupted thus, flow control coordinates the amount of data that can be sent before receiving an acknowledgment.
- **Access control:** When a single communication channel is shared by multiple devices, the MAC sub-layer of the data link layer helps to determine which device has control over the channel at a given time.

## **Network Layer – Layer 3**

The network layer works for the transmission of data from one host to the other located in different networks. It also takes care of packet routing i.e. selection of the shortest path to transmit the packet, from the number of routes available. The sender & receiver’s IP addresses are placed in the header by the network layer.
### Functions of the Network Layer 
- **Routing:** The network layer protocols determine which route is suitable from source to destination. 
- **Logical Addressing:** To identify each device on Internetwork uniquely, the network layer defines an addressing scheme. The sender & receiver’s IP addresses are placed in the header by the network layer. Such an address distinguishes each device uniquely and universally.

## **Transport Layer – Layer 4**

The transport layer provides services to the application layer and takes services from the network layer. The data in the transport layer is referred to as _Segments_. It is responsible for the End to End Delivery of the complete message. The transport layer also provides the acknowledgment of the successful data transmission and re-transmits the data if an error is found.

**At the sender’s side:** The transport layer receives the formatted data from the upper layers, performs **Segmentation**, and also implements **Flow & Error control** to ensure proper data transmission. It also adds Source and Destination port numbers in its header and forwards the segmented data to the Network Layer.

**At the receiver’s side:** Transport Layer reads the port number from its header and forwards the Data which it has received to the respective application. It also performs sequencing and reassembling of the segmented data.

Services provided by the transport layer:
1. Connection-Oriented Service
2. Connectionless Service

**1. Connection-Oriented Service:*** It is a three-phase process that includes

- Connection Establishment
- Data Transfer
- Termination/disconnection

In this type of transmission, the receiving device sends an acknowledgment back to the source after a packet or group of packets is received. This type of transmission is reliable and secure.

***2. Connectionless service:*** It is a one-phase process and includes Data Transfer. In this type of transmission, the receiver does not acknowledge receipt of a packet. This approach allows for much faster communication between devices. Connection-oriented service is more reliable than connectionless Service.

1. Data in the Transport Layer is called ****Segments****. 
2. Transport layer is operated by the Operating System. It is a part of the OS and communicates with the Application Layer by making system calls. 
3. The transport layer is called as ***Heart of the OSI*** model. 
4. **Device or Protocol Use :** TCP, UDP  NetBIOS, PPTP

## **Session Layer – Layer 5***

This layer is responsible for the establishment of connection, maintenance of sessions, and authentication, and also ensures security.

### Functions of the Session Layer

- **Session establishment, maintenance, and termination:*** The layer allows the two processes to establish, use, and terminate a connection.
- **Synchronization:*** This layer allows a process to add checkpoints that are considered synchronization points in the data. These synchronization points help to identify the error so that the data is re-synchronized properly, and ends of the messages are not cut prematurely and data loss is avoided.
- **Dialog Controller:*** The session layer allows two systems to start communication with each other in half-duplex or full-duplex.

## **Presentation Layer – Layer 6***

The presentation layer is also called the ***Translation layer***. The data from the application layer is extracted here and manipulated as per the required format to transmit over the network. 

### Functions of the Presentation Layer

- **Translation:*** For example, ASCII to EBCDIC.
- ***Encryption/ Decryption:*** Data encryption translates the data into another form or code. The encrypted data is known as the ciphertext and the decrypted data is known as plain text. A key value is used for encrypting as well as decrypting data.
- **Compression:*** Reduces the number of bits that need to be transmitted on the network.

## **Application Layer – Layer 7***

At the very top of the OSI Reference Model stack of layers, we find the Application layer which is implemented by the network applications. These applications produce the data, which has to be transferred over the network. This layer also serves as a window for the application services to access the network and for displaying the received information to the user.



| **Layer No** | **Layer Name**     | **Responsibility**                                                                                    | **Information Form(Data Unit)** | **Device or Protocol**       |
| ------------ | ------------------ | ----------------------------------------------------------------------------------------------------- | ------------------------------- | ---------------------------- |
| 7            | Application Layer  | Helps in identifying the client and synchronizing communication.                                      | Message                         | SMTP                         |
| 6            | Presentation Layer | Data from the application layer is extracted and manipulated in the required format for transmission. | Message                         | JPEG, MPEG, GIF              |
| 5            | Session Layer      | Establishes Connection, Maintenance, Ensures Authentication and Ensures security.                     | Message                         | Gateway                      |
| 4            | Transport Layer    | Take Service from Network Layer and provide it to the Application Layer.                              | Segment                         | Firewall                     |
| 3            | Network Layer      | Transmission of data from one host to another, located in different networks.                         | Packet                          | Router                       |
| 2            | Data Link Layer    | Node to Node Delivery of Message.                                                                     | Frame                           | Switch, Bridge               |
| 1            | Physical Layer     | Establishing Physical Connections between Devices.                                                    | Bits                            | Hub, Repeater, Modem, Cables |

1. TCP/IP model consists of 4 layers but OSI model has 7 layers. **Layers 5,6,7 of the OSI model are combined into the Application Layer of TCP/IP model*** and **OSI layers 1 and 2 are combined into Network Access Layers of TCP/IP protocol.**
2. The TCP/IP model is older than the OSI model, hence it is a foundational protocol that defines how should data be transferred online.
3. Compared to the OSI model, the TCP/IP model has less strict layer boundaries.
4. All layers of the TCP/IP model are needed for data transmission but in the OSI model, some applications can skip certain layers. Only layers 1,2 and 3 of the OSI model are necessary for data transmission.