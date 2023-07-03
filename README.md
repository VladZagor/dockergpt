# dockergpt
GPT model running in Docker container

Inspired by
https://github.com/imartinez/privateGPT

There are two Dockerfile:
* Dockerfile.base - downloads model, installs dependenies, etc.
* Dockerfile - copy source documents and code

For inital install - run **Dockerfile.base** and **Dockerfile** after that.

For quick updates in code or documents - run just **Dockerfile**

# Quick start
1. Build base image. It can take some time.
    > docker build -f Dockerfile.base -t dockergpt-base .
2. Copy documents to `/source_documents`. PrivateGPT supports multiple formats, but TXT, EPUB and pure HTML worked the best for me.
3. Build final image using created base image.
    > docker build -t dockergpt .
4. Run a new container
    > docker run -p 127.0.0.1:8000:8000/tcp dockergpt
5. Open http://localhost:8000/docs in browser.
6. Expand `/ask` method and click "Try it out".
7. Provide your question and click "Execute".
8. Wait for the response. It can take a few minutes.

# Reponse format

`question` - the original question that was asked.

`answer` - the answer from the model.

`sources` - documents where the model found the answer.

Always check sources if the answer is important for you - this model often hallucinates and misinterprets documents.

# Notes
This image uses GPT4All model `ggml-gpt4all-j-v1.3-groovy.bin`

It's licensed for commercial use but runs on CPU and performance is not well.

Get model details here: https://gpt4all.io/index.html

PrivateGPT also supports LLaMA that runs on GPU and should show a better performance. But looks like it's using is not legal right now. If you want to use it for research reasons, pya attention that it may require additional dependencies to be installed. Also run the container with `--gpus=all` parameter.
