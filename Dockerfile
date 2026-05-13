FROM python:3.14-alpine

RUN addgroup --system user && \
    adduser --system --ingroup user user

WORKDIR /app
COPY ./src/* .

RUN chown -R user:user /app
USER user

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/')" || exit 1

CMD ["python", "/app/server.py"]