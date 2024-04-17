# PADL

## Description

The Analytical Pipeline Definition and Deployment Language (PADL) has been specifically tailored to assist in the definition and operationalization phases of the machine learning life cycle. It provides annotations that serve as an abstraction layer from the underlying infrastructure and technologies, hence facilitating the work of data scientists and engineers. Due to its proficiency in the operationalization of distributed pipelines over edge, fog, and cloud layers. PADL contains functionalities for the specification of monitoring, notifications, and actuation capabilities.

## Install

The recommended way to install PADL is by building the corresponding docker images. This repository includes two different tools, the CLI and the Web Linter. To utilize the CLI please use the following steps.

```bash
cd lib
docker build . -f Dockerfile-cli -t padl-cli

```

To utilize the web linter please use the following steps.

```bash
cd lib
docker build . -f Dockerfile-web -t padl-web
docker run -p 5000:5000 padl-web
```

Navigate to localhost:5000 and start validating the PADL documents.

## Contributing

Contributions are always welcome! Please read the [contribution guidelines]([Contributing to a project - GitHub Docs](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)) first.

## License

See the [LICENSE]([padl/LICENSE at master · josu-arcaya/padl · GitHub](https://github.com/josu-arcaya/padl/blob/master/LICENSE)) file for licensing information.
