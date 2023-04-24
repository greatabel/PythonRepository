```mermaid
graph TD
    A[Chinese-LLaMA-Alpaca] --> B[Prompts]
    A --> C[LLMs]
    A --> D[Chains]
    A --> E[Agents]
    A --> F[Memory]
    A --> G[Chat]
    C --> H[Moss-003]
    C --> I[Vicuna 7B Model]
    J[HX_Gpt app and api] -->|uses| B
    J -->|uses| C
    J -->|uses| D
    J -->|uses| E
    J -->|uses| F
    J -->|uses| G
    H -->|integrated with| J
    I -->|integrated with| J

    style A fill:#f9d6c1,stroke:#f66,stroke-width:2px;
    style B fill:#f9f2c1,stroke:#d6b656,stroke-width:2px;
    style C fill:#d9f9c1,stroke:#68b83e,stroke-width:2px;
    style D fill:#c1f9d6,stroke:#58a99a,stroke-width:2px;
    style E fill:#c1d6f9,stroke:#5662b8,stroke-width:2px;
    style F fill:#f9c1f3,stroke:#b853b3,stroke-width:2px;
    style G fill:#f5f5f5,stroke:#c1c1c1,stroke-width:2px;
    style H fill:#d9c1f9,stroke:#a358b8,stroke-width:2px;
    style I fill:#f9c1c1,stroke:#b85656,stroke-width:2px;

# pandoc -f markdown -t html i3draw_flow_chart_input.md -o i3output.html