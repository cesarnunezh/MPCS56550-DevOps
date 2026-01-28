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
