# diagram_as_code_python

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



## 1. 

<img width="1269" alt="Screenshot 2023-11-28 at 18 00 43" src="https://github.com/otam-mato/diagram_as_code_python/assets/113034133/6eac2c55-9016-4521-bad8-3f710258c7c6">

<br><br>

```python3
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

with Diagram("Clustered Web Services", show=False, direction="TB"):
    dns = Route53("AWS Route53")
    lb = ELB("AWS ELB")

    with Cluster("Services(on ECS)"):
        svc_group = [ECS("service1"),
                     ECS("service2"),
                     ECS("service3")]

    with Cluster("DB Cluster"):
        db_primary = RDS("RDS")
        db_primary - [RDS("RDS ReadOnly")]

    memcached = ElastiCache("ElastiCache")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached
```
