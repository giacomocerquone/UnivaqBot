## System Requirements Specification (SRS)


Introduction
************

Step Ladder is a software framework for the OLPC laptop that provides universally useful tools that leverage the OLPC architecture and allow it to be used as an educational tool in the classroom in developing nations.  The end goal is to provide functionality that will allow it to be used in schools that currently do not know what to do with it.

Purpose
-------

univaq-bot is a open source project

Scope
-----

The software we are providing is a universally useful tool for OLPC, but for context and background we are working with an organization in Uganda that has 100 untouched OLPC laptops.  Our goal is to provide the functionality that will give teachers a way to put those laptops into use.

**Deliverable**:  Educational game and familiarization software that explain how to make use of the laptop.

**Benefits**:  Gives teachers an added tool for the classroom and students an exciting educational experience.

Definitions, acronyms, and abbreviations 
----------------------------------------

OLPC
   One Laptop Per Child

XO
    The name of the OLPC laptop.

XO 1.0
   Laptop version that was provided up to Fall 2009

XO 1.5
   Updated version shipped out in Fall 2009

XO 2.0
   Touch screen version planned for Fall 2010

Sugar
   XO operating system based off Fedora OS

Activities
   Software applications for Sugar

References 
----------

* https://www.python.org/dev/peps/pep-0008/ - Style Guide for Python Code
* :pep:`257` - Docstring Conventions
* `OLPC home page <http://laptop.org/en/>`_
* `OLPC Wiki <http://wiki.laptop.org/>`_
* `IEEE 830 (Software Requirements Specification) <http://standards.ieee.org/reading/ieee/std_public/description/se/830-1998_desc.html>`_

.. This subsection should 

.. a. Provide a complete list of all documents referenced elsewhere in
.. the SRS;

.. b. Identify each document by title, report number (if applicable),
.. date, and publishing organization;

.. c. Specify the sources from which the references can be obtained.
.. This information may be provided by reference to an appendix or to
.. another document.

.. CS401 NOTE: This is not the same thing as a list of the documents in your literature review; however, many of them may end up here, too.

Overview
--------
* Overall Description
   + Product Perspective
   + Interfaces
   + Product Function
   + Constraints
   + Assumptions

* Specific Requirements (Organized by feature)
   + External
   + Functional
   + Performance

.. This subsection should 

.. a. Describe what the rest of the SRS contains; 

.. b. Explain how the SRS is organized. CS401 NOTE: Describe which organization you will be using for section 3. 

Overall Description
*******************

Product Perspective
-------------------

The Step Ladder project fits into the OLPC framework as an interface with the user in the classroom and the existing laptop functionality as shown in the diagram below:

.. This section should put the product in perspective with other related products. If the product is independent and totally self-contained, it should be so stated here. If the SRS defines a product that is a component of a larger system, then this subsection should describe the relationship between the two. 
.. A block diagram showing the major components of the larger system, interconnections, and external interfaces should be provided here. 
.. This subsection should also describe how the software operates inside various constraints. For example, these constraints could include the following interfaces:

.. CS401 Note: The interfaces described here are associated with things external to the system being developed.  The following sections should describe what you, as developers, need to know about the external systems to interface with them.
.. CS401 Note: If your project is multi-disciplinary, this is the place to clearly define how your system will interface with the parts/modules being built by the other disciplinary teams. Naturally, their documentation should include the same interface specification and all of them should be kept consistent.

System interfaces
^^^^^^^^^^^^^^^^^

The software is designed for use on the XO laptops in educational environments in developing nations.

.. This should list each system interface and identify the functionality of the software to accomplish the system requirement and the interface description to match the system.

.. _user_interfaces:

User interfaces
^^^^^^^^^^^^^^^

The XO has two primary users – the teachers who use it as a tool for the classroom and the students themselves.

Teachers
""""""""

The Teacher Tutorial guides the teacher through the functionality of the XO that can be leveraged in the classroom.  After going through this tutorial a teacher should have the basic knowledge to use the laptops in their curriculum.

Students
""""""""

The educational software interfaces directly with the student.  The application we are providing is Tetris Math, a head to head multiplayer math game.

We are also providing a User Startup Tutorial that forces the user to experiment with touchpad, keyboard, and GUI of the XO the first time using the laptop.  After going through this tutorial, users first grade and should understand how to use the touchpad and keyboard, and how to navigate the basics of the Sugar user interface.

Finally the Wiki Help Framework is a help framework for all of the activities and functions of the XO, designed wiki-style so that teachers can update it so that it relates directly to them and their students.  A teacher with limited technical experience should be able to update this help framework, and it should be accessible for all users to view.

.. This should specify the following: 

.. a. The logical characteristics of each interface between the software product and its users. This includes those configuration characteristics (e.g., required screen formats, page or window layouts, content of any reports or menus, or availability of programmable function keys) necessary to accomplish the software requirements. 

.. b. All the aspects of optimizing the interface with the person who must use the system. This may simply comprise a list of do's and don'ts on how the system will appear to the user. One example may be a requirement for the option of long or short error messages. Like all others, these requirements should be verifiable, e.g., "a clerk typist grade 4 can do function X in Z min after 1 hour of training" rather than "a typist can do function X." (This may also be specified in the Software System Attributes under a section titled Ease of Use.) 

Hardware interfaces
^^^^^^^^^^^^^^^^^^^

Touchpad
   Used for moving the pointer on-screen
Keyboard
   Used for text input
Directional pad and game buttons
   Used in Tetris Math when played tablet-style

.. This should specify the logical characteristics of each interface between the software product and the hardware components of the system. This includes configuration characteristics (number of ports, instruction sets, etc.). It also covers such matters as what devices are to be supported, how they are to be supported, and protocols. For example, terminal support may specify full-screen support as opposed to line-by-line support.

Software interfaces
^^^^^^^^^^^^^^^^^^^

Sugar OS: All applications run within the Sugar operating system environment.

.. This should specify the use of other required software products (e.g., a data management system, an operating system, or a mathematical package), and interfaces with other application systems (e.g., the linkage between an accounts receivable system and a general ledger system). For each required software product, the following should be provided: 
.. Name 
.. Mnemonic 
.. Specification number 
.. Version number 
.. Source 
.. For each interface, the following should be provided: 
.. Discussion of the purpose of the interfacing software as related to this software product. 
.. Definition of the interface in terms of message content and format.  It is not necessary to detail any well-documented interface, but a reference to the document defining the interface is required. 

Communications interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^

OLPC Mesh School Server provides wireless interconnectivity between laptops in a classroom and provides the framework needed for multiplayer Tetris Math.

.. This should specify the various interfaces to communications such as local network protocols, etc.

Memory
^^^^^^

N/A

.. This section should specify any applicable characteristics and limits on primary and secondary memory.

Operations
^^^^^^^^^^

.. See :ref:`User Interfaces <user_interfaces>`.

See User Interfaces.

.. This section should specify the normal and special operations required by the user such as 
.. a.The various modes of operations in the user organization (e.g., user-initiated operations); 
.. b.Periods of interactive operations and periods of unattended operations; 
.. c.Data processing support functions; 
.. d.Backup and recovery operations. 
.. NOTE: This is sometimes specified as part of the User Interfaces section.

Site adaptation requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The OLPC program is implemented in developing nations with little infrastructure.  At a minimum the XO requires electrical supply or some means of charging the battery (one instance of batteries charged by pedal power in Afghanistan).  In our case study with Uganda, there is electricity, but no access to the internet in the classroom.

.. This section should 
.. a.Define the requirements for any data or initialization sequences that are specific to a given site, mission, or operational mode (e.g., grid values, safety limits, etc.); 
.. b.Specify the site or mission-related features that should be modified to adapt the software to a particular installation. 

.. _product-function-lablel:

Product Functions
-----------------

The diagram below shows an overview of the functions our software provides:

.. Provide a summary of the major functions that the software will perform. This is an outline of the functional requirements in section 3.1, so don’t be too specific here. 
.. Note that for the sake of clarity 

.. a. The functions should be organized in a way that makes the list of functions understandable to the customer or to anyone else reading the document for the first time. 

.. b. Textual or graphical methods can be used to show the different functions and their relationships. Such a diagram is not intended to show a design of a product, but simply shows the logical relationships among variables. 

User Characteristics
--------------------

Teachers
^^^^^^^^

Educators in developing nations. May have had little or no prior experience with computers.

Students
^^^^^^^^

First and second grade students in developing nations.  Most have no prior experience with computers.

.. Describe the general characteristics of the intended users including educational level, experience, and technical expertise.  It should not be used to state specific requirements, but rather should provide the reasons why certain specific requirements are later specified in Section 3 of the SRS.

Constraints
-----------

Processing power of the XO laptop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All software will have to be designed to function within the constraints of the XO hardware.

Lack of Internet access
^^^^^^^^^^^^^^^^^^^^^^^
We must assume that there is no internet access where the software will be used, so we cannot rely on net-based software updates or help resources.

Societal Implications
^^^^^^^^^^^^^^^^^^^^^
The overall goal of OLPC is to provide an educational tool that a child can use to connect to the rest of the world and exercise the potential within them.  This will hopefully have a significant positive societal impact on communities in developing nations where the groundwork is being laid for future leaders to make a difference and bring economic growth to their communities.  However within the whole project it must be remembered that there are significant cultural differences that may affect the way this technology is received, so it is important to make an effort to understand these differences and how to best apply technology in these areas.

Political Implications
^^^^^^^^^^^^^^^^^^^^^^
OLPC as an organization works closely with the governments and education ministries of developing nations where the laptops are distributed.  There are several countries that have expressed interest in OLPC, but are waiting to see the results of the program in other countries.  If what we provide adds to the success of OLPC in the nations where it is already deployed, it can have an even further reaching affect by garnering support from additional countries and connecting more children with this program.

Economic Implications
^^^^^^^^^^^^^^^^^^^^^
This program is hopefully the first step in providing useful technical skills for an upcoming generation in developing countries.  This could hopefully lead to the rise of a middle class in countries that have never experienced it.

.. Specify here any issues that will limit the developer’s options. 
.. These include:
.. a. Regulatory policies; 
.. b. Hardware limitations (e.g., signal timing requirements); 
.. c. Interfaces to other applications; 
.. d. Parallel operation; 
.. e. Audit functions; 
.. f. Control functions; 
.. g. Higher-order language requirements; 
.. h. Signal handshake protocols (e.g., XON-XOFF, ACK-NACK); 
.. i. Reliability requirements; 
.. j. Criticality of the application; 
.. k. Safety and security considerations. 

.. CS401 Requirement:  In this section you are also required to include the following analyses:
.. 1. Societal Implications 
.. 2. Political Implications 
.. 3. Economic Implications 

Assumptions and dependencies
----------------------------

* Electrical power in areas where the XO will be used
* Cultural acceptance of laptops as educational tools

.. This section of the SRS should list each of the factors that affect the requirements stated in the SRS. These factors are not design constraints on the software.  Rather, they are any changes to them that can affect the requirements in the SRS. For example, an assumption may be that a specific operating system will be available on the hardware designated for the software product.
.. Many of these assumptions will be become part of the basis of your risk-mitigation strategy.

Apportioning of requirements
----------------------------

Section 2.2 (product function) lays out the priority of the requirements for this project.  The last requirement to be completed is the Wiki Help Framework, and this can be delayed for future visitations of this project.  Other future work includes additional educational software applications and a framework for updates in areas that do not have access to the Internet.

.. This section should identify requirements that may be delayed until future versions of the system.  A necessary part of the process is to identify all of the requirement, estimate the effort required, and prioritize the requirements.  This section will identify known requirements that will not be incorporated into the system describe by this SRS.

Specific Requirements
*********************
	
.. This section of the SRS should contain all of the software requirements to a level of detail sufficient to enable designers to design a system to satisfy those requirements, and testers to test that the system satisfies those requirements. Throughout this section, every stated requirement should be externally perceivable by users, operators, or other external systems. These requirements should include at a minimum a description of every input (stimulus) into the system, every output (response) from the system, and all functions performed by the system in response to an input or in support of an output. As this is often the largest and most important part of the SRS, the following principles apply: 

.. a. Specific requirements should be stated in conformance with all the characteristics described in 4.3. 

.. b. Specific requirements should be cross-referenced to earlier documents that relate. 

.. c. All requirements should be uniquely identifiable. 

.. d. Careful attention should be given to organizing the requirements to maximize readability. 

External interface requirements
-------------------------------

.. For most systems, this section addresses issues pertaining to the (graphical) user interface (e.g. which versions of web browsers must be supported). It may also discuss the interfaces to other external (existing) systems. For embedded systems, this describes the interface requirements for the hardware and/or other software subsystems. 
.. This should be a detailed description of all inputs into and outputs from the software system. It should complement the interface descriptions in Section 2 (user, hardware, software, and communications interfaces) and should not repeat information there.
.. CS401 Note:  Remember those "interfaces with the external system" from section 2?  This section is where you will specify the requirements for those interfaces within your system.  For example, if part of the external system is a servo that requires a particular kind of signal to operate, this section will describe the requirements for producing that signal.

User interfaces
^^^^^^^^^^^^^^^

* All OLPC laptops are equipped with Python 2.5 and PyGame, and any external libraries can be bundled with the program.
* Applications will use the Sugar library for all GUIs.

.. Requirements for interaction with user interfaces.

Hardware interfaces
^^^^^^^^^^^^^^^^^^^

* OLPC laptops use standardized hardware, so there will be no compatibility issues.
* The hardware interface is exposed through Python libraries.

Software interfaces
^^^^^^^^^^^^^^^^^^^

* Python 2.5 is required.
* The PyGame python library is required because is provides access to graphics drivers.
* Other required libraries can be bundled with applications.

.. Requirements for interaction with software interfaces.

Communications interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^

* The XO can access a variety of different Wireless Access Points. [#wap]_
* The mesh networking capability is exposed by a Python API. [#api_ref]_

.. Requirements for interaction with communications interfaces.

Functional Requirements
-----------------------

.. Functional requirements should define the fundamental actions that must take place in the software in accepting and processing the inputs and in processing and generating the outputs. 
.. Requirements must be written in the format: “x will/shall/must y” or “Given a, x will/shall/must y.” 
.. Each requirement must address only one measurable and testable portion of your project. 
.. It may be appropriate to partition the functional requirements into sub-functions or sub-processes. This does not imply that the software design will also be partitioned that way.
.. This should be, by far, the longest section of your document. Be sure to address each requirement of your system, no matter how trivial it may seem.
.. CS401 NOTE:  The IEEE SRS standard - Annex A - provides several different templates for organizing the requirements (by object, by feature, etc.).  You should review these and either use the one that seems most appropriate for your project, or develop one of your own.

OLPC Laptop Requirements
^^^^^^^^^^^^^^^^^^^^^^^^

* The user must have an OLPC laptop.
* The OLPC laptop must have a working keyboard.
* The OLPC laptop must have a working display.
* The OLPC laptop must have a working webcam.
* The OLPC laptop must have a working touchpad.
* The OLPC laptop must have a working d-pad.
* The OLPC laptop must have working sound.
* The OLPC laptop must have Python 2.5 and PyGame.
* The OLPC laptop must have mesh capability with other OLPC laptops.
* The OLPC laptop must be able to connect to an OLPC server.

OLPC Server Requirements
^^^^^^^^^^^^^^^^^^^^^^^^

* Given an OLPC server , it must provide network access to OLPC laptops.
* Given an OLPC server, it must be able to store data from OLPC laptops.

Tetris Math Requirements
^^^^^^^^^^^^^^^^^^^^^^^^

* Given an OLPC laptop, Tetris Math must be installed.
* Tetris Math will provide a Sugar GUI.
* Tetris Math will provide a single player game.
* Given a mesh network of other OLPC laptops, Tetris Math will multiplayer capabilities for 1 - 4 users.

User Startup Tutorial Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Given and OLPC laptop, the Startup Tutorial must be installed.
* When the OLPC laptop starts, the Startup Tutorial will run.
* The Startup Tutorial will provide options to enable/disable it.
* The Startup Tutorial will provide the ability to be remotely enabled from the OLPC server.
* The Startup Tutorial must be allowed to run at any time.
* The Startup Tutorial must provide a demonstration of the following: 
    + Start an application.
    + Close an application.
    + Switch applications.
* The startup Tutorial must provide illustrations of the following OLPC hardware capabilities:
    + Start the OLPC laptop.
    + Shutdown the OLPC laptop.
    + Adjust the volume.
    + Movement with the d-pad.
    + Rotate the OLPC screen to a tablet view.

Performance Requirements
------------------------

* Tetris Math must provide smooth performance to end users.
* The OLPC server must support at least 20 users.

.. This subsection should specify both the static and the dynamic numerical requirements placed on the software or on human interaction with the software as a whole. Static numerical requirements may include the following: 
.. a. The number of terminals to be supported; 

.. b. The number of simultaneous users to be supported; 

.. c. Amount and type of information to be handled. 
.. Static numerical requirements are sometimes identified under a separate section entitled Capacity. 
.. Dynamic numerical requirements may include, for example, the numbers of transactions and tasks and the amount of data to be processed within certain time periods for both normal and peak workload conditions. 
.. All of these requirements should be stated in measurable terms. 
.. For example, 
.. 95% of the transactions shall be processed in less than 1 s. 
.. rather than, 
.. An operator shall not have to wait for the transaction to complete. 
.. NOTE: Numerical limits applied to one specific function are normally specified as part of the processing sub-paragraph description of that function.

Design constraints
------------------

* Target OLPC laptops in Africa are difficult to update, so the code must be robust.
* Python is a relatively slow language.  Algorithms must be chosen carefully to avoid excessive slowdowns.
* OLPC laptops use 433 Mhz CPU optimized for battery life rather than speed. [#olpc_spec]_  Applications must be designed to utilize limited hardware.

Software system attributes
--------------------------

Reliability
^^^^^^^^^^^

* Code must be robust, and fail gracefully.

Availability
^^^^^^^^^^^^

* All code is open source.
* The OLPC project and all software it uses is open source.

.. Requirements for availability of the system or the information it handles.

Security
^^^^^^^^

* The OLPC laptops will run on a private network.  There is no security threat from outside the network.
* Data stored on the OLPC server provides limitied security.

Maintainability
^^^^^^^^^^^^^^^

* Code is documented using standard Python practices, including function docstrings (:pep:`257`) and the use of Restructured Text.
* Code is written in standard Python style (:pep:`8`).

Portability
^^^^^^^^^^^

* The code targets only the OLPC laptop.
* DeSugarized applications should run on any computer with Python 2.5.

Other Requirements
------------------

.. Place any requirements that don't logically fit elsewhere into this section.
.. Appendices 
.. The appendices are not always considered part of the actual SRS and are not always necessary. They may include 

..       a. Sample input/output formats, descriptions of cost analysis studies, or results of user surveys; 

..       b. Supporting or background information that can help the readers of the SRS; 

..       c. A description of the problems to be solved by the software; 

..       d. Special packaging instructions for the code and the media to
..       meet security, export, initial loading, or other requirements.

.. When appendices are included, the SRS should explicitly state whether or not the appendixes are to be considered part of the requirements.
.. CS401 Note: There will probably many collections of information for your project well suited for inclusion in an appendix vice the main body. Don't hesitate to use appendices.
.. Index
.. List the major terms from this document and provide a hyperlink to a bookmark at that point (don't use page numbers on a website!).

Appendices
**********

.. The appendices are not always considered part of the actual SRS and are not always necessary. They may include 
.. a. Sample input/output formats, descriptions of cost analysis studies, or results of user surveys; 

.. b. Supporting or background information that can help the readers of the SRS; 

.. c. A description of the problems to be solved by the software; 

.. d. Special packaging instructions for the code and the media to meet security, export, initial loading, or other requirements. 

.. When appendices are included, the SRS should explicitly state whether or not the appendixes are to be considered part of the requirements.

.. CS401 Note: There will probably many collections of information for your project well suited for inclusion in an appendix vice the main body.  Don't hesitate to use appendices.


Index
*****

.. [#wap] `Wireless Access Point Compatibility <http://wiki.laptop.org/go/Wireless_Access_Point_Compatibility>`_
.. [#olpc_spec] `XO Hardware Specification <http://wiki.laptop.org/go/Hardware_specification>`_
.. [#api_ref] `OLPC API Reference <http://wiki.laptop.org/go/API_Reference>`_
.. List the major terms from this document and provide a hyperlink to a bookmark at that point (don't use page numbers on a website!)
