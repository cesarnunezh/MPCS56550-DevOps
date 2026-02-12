# Lecture 01: DevOps Introduction 

Why DevOps?
- Shared knowledge
- Organization: agreements, defining processes takes time.
- Delays on integration (incorrect use of interfaces, library versions, development environments)
- Testing: manual testing takes time.
- Lose time, lose opportunities, market share vs competitors.

DevOps principles:
- Everyone is responsible for everything
- Everything that can be automated should be

Components
- DevOps Automation:
- Code management system
- DevOps Measurement

Benefit of DevOps
- Reduced risk: Not wait until the last minute to face problems on deployment. 
- Faster deployment:
- Faster repair: fix it quickly.
- More productive teams: 

DevOps processes:
- Design: take insights to design
- Dev: code it
- Build: make your code executable, see inconsistencies 
- Test: 
- Release: make all documentation needed
- Deploy:
- Operates:
- Monitor & Analyze: logs to monitorized.

# Lecture 03: Continuous Integration

Deployment process:
- Development: Coding, containerization, unit tests.
- Integration: Integrates different pieces of code into one.
- Stagging: Test from the user perspective. QA/Smoke tests (major features are working)
- Production: Continuous delivery. Needs approval.

Elements of the environment
- Virtual machines or containers
- Infrastructure services (e.g. load balancer/ gateway/ cache)
- A source of input for runtime tests
- Data management system (Database)
- configuration parameters
- external services


Development environment:
- Code development -> clone repo, create feature branch, write code and unit tests
- Local testing -> Run unit tests, debug, validate functionality locally
- Code Quality -> Run linters, static analysis, and security scans
- Version Control -> Commit changes, push branch, create pull request
- Code Review -> Peer review and feedback incorporation.

    Unit tests:
        - Sunny-day tests conditions: expected situations
        - Rainy-day tests: unexpected situations
        - Regression tests: 

Integration environment:
- Code Merge -> approved pull requests merged into main/develop branch
- Automated Trigger -> CI pipeline triggered by merge or scheduled intervals
- Build Process -> Compile code, resolve dependencies, create artifacts.
- Automated Testing -> Run comprehensive test suites (unit, integration, API tests)
- Quality Gates -> Code coverage, security scans, performance benchmarks
- Environment Provisioning -> Spin up integration with required services 
- System Integration Testing -> Test complete system with all components integrated
- Cross-Component Testing -> Verify interactrions between different modules
- Test Reporting
- Environment Cleanup


# Lecture 4: Continuous Development

User testing -> analyze a real case use of the application
App load testing (scalability)

Staging Environment Workflow Steps:
- Artifact Promotion
- Production-Like Deployment: update other services / migration scripts
- Environment Validation: Mirror production configuration
- Data Refresh: Load production-like data or sanitized production data subsets
- User Acceptance Testing (UAT): Business users validate features meet requirements.
- Performance Testing: Load testing, stress testing and performance benchmarking
- Security Testing: penetration testing, vulnerability assessments, scurity scans
- Regression Testing: ensure new changes don't break existing funcionalities
- Infrastructure Testing: validate deployments scripts, database migrations, configurations
- Monitoring Validation: Test alerting, logging, monitoring systems
- Release Documentation: Finalize release notes, deployment guides, rollback procedures.

Qualities of the pipeline
- Cycle time: It should tell you right away
- Traceability: you're able to know what stage fail and where it fails
- Repeadability: It gives you the same result from the same stage.
- Security: 

# Lecture 5: Container Orchestration

### Deployment strategies:
- Blue/Green: Copy all the containers and just delete them when all users has migrated
- Rolling Upgrade: Copy all the containers but delete them as each container has all users migrated from

### Roll back/forward
- Roll back: go back to a previos version of the app
- Roll fordward: push something with failures -> fix it and deploy a new working version

### Partial deployments
- Canary testing: similar to the rolling testing, but we are testing getting feedback and then expanding 
- A/B Testing: Testing some tweaks to the application to improve.

