## Slide 8

- $0 cost for idle infrastructure through scale-to-zero execution.
- Pay-per-use billing down to the millisecond, aligning cost exactly with traffic.
- Instant horizontal elasticity: thousands of concurrent events automatically create thousands of parallel instances.
- Eliminates idle waste typical in provisioned VM capacity models.

## Slide 9

- Keep functions single-purpose to reduce memory footprint and execution time.
- Externalize state using low-latency key-value stores instead of slow relational databases.
- Use Provisioned Concurrency for latency-sensitive user endpoints.
- Avoid monolithic function designs and complex workflow orchestration inside a single function.

## Slide 10

- Kubernetes charges for reserved capacity, while serverless charges per execution duration.
- Serverless containers combine container portability with the simplicity of FaaS.
- Reduce operational overhead by eliminating cluster and node management.

Platforms include AWS Fargate, Google Cloud Run, and Knative.
## Slide 11
This slide shows where cloud programming is heading beyond basic serverless functions.

- **Advanced Resource Management and Sustainability**: 
    - Auto-scaling algorithms that use predictive modeling to optimize resource provisioning.
    - Dynamic power and energy management scheduling to reduct environmental impact.

- **Evolution Toward Stateful Serverless**: 
    - Move beyond stateless model to Stateful Serverless
    - Functions can maintain and access data across invocations.
    - Support complex distributed workflows, transactional support, and data-dependent applications that require consistency and durability.

- **Solving the Cold-Start Problem**: 
    - Warm-start strategies with pre-heated instances and predictive modeling to allocate resources before they are needed.
    - Container reuse and recycling to minimize environmente setup overhead.

- **Expansion into Edge Computing and Machine Learning**: 
    - Optimizing serverless for ML-driven workloads beyond Internet of Things (IoT). 
    - Deep learning inference with GPUs and LLMs