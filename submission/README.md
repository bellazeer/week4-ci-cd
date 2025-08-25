# Week4 Docker Ci Submission

## 📁 Submission Contents

This folder contains your Week4 Docker Ci assignments.

### Required Files
- [ ] Add your required files here
- [ ] Based on the weekly requirements
- [ ] Check the main README.md for details

### Submission Checklist
- [ ] All requirements completed
- [ ] Code quality standards met
- [ ] Documentation is complete
- [ ] Tests are passing
- [ ] Ready for review

## 🚀 How to Run

1. Set up environment
cp submission/.env.example submission/.env

2. Install dependencies
pip install -r submission/requirements.txt

3. Run the FastAPI app
uvicorn submission.main:app --reload

4. Run with docker
docker build -t week4_app submission/
docker run -p 8000:8000 week4_app


## 📊 Results Summary

1. All unit tests passed 

2. Security scan completed without major issues

3. Docker container builds successfully

4. CI/CD workflow triggers correctly on push to main (after .github/workflows/deploy.yml is moved to the root)

## 🎯 Learning Outcomes

1. Learned how to set up a CI/CD pipeline using GitHub Actions

2. Managed Python environment and dependencies

3. Ran unit tests and security scans effectively

4. Built and deployed a Docker container for a FastAPI app

5. Gained practical experience in repository structure for GitHub Actions workflows
