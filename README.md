# 🚀 Go (Golang) Learning Roadmap

Track your progress while learning Go.  
You can use this file directly or convert each section into GitHub Issues with checklists.

## 📋 Creating Issues for Learning Sections

This repository includes GitHub issue templates for each learning section. You can create issues in two ways:

### Option 1: Automated Script (Recommended)
Run the provided script to create all issues at once:
```bash
./create-learning-issues.sh
```

### Option 2: Manual Creation
1. Go to the [Issues tab](../../issues)
2. Click "New Issue"
3. Select the appropriate template for the section you want to track
4. Customize the title and add any additional notes
5. Create the issue

Each issue template includes:
- ✅ Complete checklist of learning objectives
- 📚 Relevant resources and documentation links
- 📝 Space for your notes and code examples

---

## 🟢 1. Go Basics (Language Core)
- [ ] Setup & Tooling (`go run`, `go build`, `go mod`)
- [ ] Project structure & modules
- [ ] Variables, constants, type inference (`:=`)
- [ ] Basic types: string, int, float, bool, rune, byte
- [ ] Type conversions
- [ ] Control Flow (`if`, `for`, `switch`, break/continue)
- [ ] Functions (multiple return values, named return values, variadic)
- [ ] Pointers (value vs reference, passing by reference)

---

## 🟡 2. Data Structures & Collections
- [ ] Arrays & Slices (length, capacity, backing array, append, copy, slicing)
- [ ] Maps (declaration, CRUD, check existence with `value, ok := map[key]`)
- [ ] Structs (initialization, field tags, embedding)
- [ ] Methods (value vs pointer receivers)

---

## 🟠 3. Deeper Language Features
- [ ] Interfaces (implicit implementation, empty interface, type assertions)
- [ ] Error Handling (`error` type, custom errors, `errors.Is`, `errors.As`, `fmt.Errorf` with `%w`)
- [ ] Packages (`init()`, exported vs unexported)
- [ ] Generics (type parameters, constraints) — Go 1.18+
- [ ] Reflection (`reflect` package basics)

---

## 🔵 4. Concurrency & Parallelism
- [ ] Goroutines (lightweight threads, function calls as goroutines)
- [ ] Channels (unbuffered vs buffered, `select` statement)
- [ ] Concurrency Patterns (worker pools, fan-in / fan-out, context cancellation)
- [ ] `sync` Package (WaitGroup, Mutex, RWMutex, Once)
- [ ] Atomic operations

---

## 🟣 5. Standard Library & Utilities
- [ ] I/O & Files (`io`, `os`, `bufio`)
- [ ] Strings & Formatting (`strings`, `strconv`, `fmt`)
- [ ] Time (`time` package, timers, tickers)
- [ ] Networking (`net/http` basics, JSON handling with `encoding/json`)
- [ ] Testing (`testing` package, table-driven tests, benchmarks & examples)

---

## 🔴 6. Advanced Topics
- [ ] Context (`context.Background`, `WithCancel`, `WithTimeout`)
- [ ] Error Groups (`errgroup` package)
- [ ] Custom Packages & Modules (semantic versioning, private modules)
- [ ] Performance (profiling with `pprof`, escape analysis)
- [ ] Memory Management (garbage collection basics)

---

## 🟤 7. Go in Practice
- [ ] Web Development (`net/http`, frameworks: Fiber, Gin, Echo)
- [ ] Database (`database/sql`, ORMs: GORM, Ent)
- [ ] Microservices (gRPC, REST APIs)
- [ ] Deployment (building executables, cross-compilation, Dockerizing Go apps)

---

## ⚫ 8. Ecosystem & Best Practices
- [ ] Go Modules & Dependency Management
- [ ] Project structure (standard layout)
- [ ] Logging (`log`, `zap`, `zerolog`)
- [ ] Configuration management (`viper`)
- [ ] Linters & formatters (`gofmt`, `golangci-lint`)
- [ ] CI/CD pipelines
- [ ] Security practices (validations, safe concurrency)
