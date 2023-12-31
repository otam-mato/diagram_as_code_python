# Diagram As Code (using Python)

<br>

> **Note:** Declarative diagramming involves the creation of diagrams through a declarative approach, encompassing a range from flowcharts to organization charts. In this methodology, users define the relationships and logic of the diagram's elements using a formal language, as opposed to the traditional method of manually placing and connecting shapes on a canvas.
>
> While this approach may not be the most practical for sporadically generating individual diagrams, it proves highly advantageous for automation processes reliant on reusable templates and their seamless customization.

<br>

## Technologies used
- **Diagram-As-Code**
- **Python 3**
- **Linux**
  
<br>



## 1. A clustered architecture example created with a Python script

<img width="1269" alt="Screenshot 2023-11-28 at 18 11 30" src="https://github.com/otam-mato/diagram_as_code_python/assets/113034133/03998a26-d776-4dd6-bbdf-6e1d31a90796">

<br><br>

```python3
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

with Diagram("ECS Clustered Services", show=False, direction="TB", graph_attr={"labelloc": "t"}):
    dns = Route53("AWS Route53")
    lb = ELB("AWS ELB")

    with Cluster("ECS cluster"):
        svc_group = [ECS("web1"),
                     ECS("web2"),
                     ECS("web3")]

    with Cluster("AWS RDS Cluster"):
        db_primary = RDS("RDS")
        db_primary - [RDS("RDS ReadOnly")]

    memcached = ElastiCache("AWS ElastiCache")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached
```

<br>

## 2. Event Processing on AWS example created with a Python script

<img width="1269" alt="Screenshot 2023-11-28 at 19 33 44" src="https://github.com/otam-mato/diagram_as_code_python/assets/113034133/508cfce0-aa89-4af7-991b-fafa553d4126">

<br><br>

```python3
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

with Diagram("Event Processing", show=False, graph_attr={"labelloc": "t"}):
    source = EKS("EKS source")

    with Cluster("Event Flows"):
        with Cluster("Event Workers"):
            workers = [ECS("service1"),
                       ECS("service2"),
                       ECS("service3")]

        queue = SQS("AWS SQS event queue")

        with Cluster("Processing"):
            handlers = [Lambda("process1"),
                        Lambda("process2"),
                        Lambda("process3")]

    store = S3("S3")
    dw = Redshift("Redshift")

    source >> workers >> queue >> handlers
    handlers >> store
    handlers >> dw
```

<br>

## Prerequisites

- **A work station / Virtual machine (I am using UBUNTU 22.04)**
- **Python 3** installed.
- **pip** installed.

<br>

## Steps:

### 1. Install the `diagrams` module

```py
pip install diagrams
```
The "diagrams" library in Python is used for creating infrastructure-as-code diagrams.

### 2. Install `graphviz` 

```py
sudo apt-get install graphviz
```
`Graphviz` is an open-source software tool used for the visualization of graphs and networks. A graph, in this context, refers to a collection of nodes and edges that connect pairs of nodes. 

### 3. Create or copy the script 

[ diagr.py ](https://github.com/otam-mato/diagram_as_code_python/blob/94db1bc5becec7e0d012f556d74c4608f5aebab9/diagr.py)

### 4. Launch the script 

```py
python3 diagr.py
```

### 5. Open the generated `ecs_clustered_services.png` file to check the diagram (I am using the default image viewer in Ubuntu called "Eye of GNOME" (eog), make sure it is installed)

```py
eog ecs_clustered_services.png
```
