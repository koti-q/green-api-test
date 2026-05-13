const apiUrl = "https://api.green-api.com";

function getCredentials() {
  const idInstance = document.getElementById("idInstance").value;
  const apiTokenInstance = document.getElementById("apiTokenInstance").value;

  return { idInstance, apiTokenInstance };
}

function showResponse(data) {
  document.getElementById("response").value =
    JSON.stringify(data, null, 2);
}

async function getSettings() {
  const { idInstance, apiTokenInstance } = getCredentials();

  const response = await fetch(
    `${apiUrl}/waInstance${idInstance}/getSettings/${apiTokenInstance}`
  );

  const data = await response.json();

  showResponse(data);
}

async function getStateInstance() {
  const { idInstance, apiTokenInstance } = getCredentials();

  const response = await fetch(
    `${apiUrl}/waInstance${idInstance}/getStateInstance/${apiTokenInstance}`
  );

  const data = await response.json();

  showResponse(data);
}

async function sendMessage() {
  const { idInstance, apiTokenInstance } = getCredentials();

  const chatId = document.getElementById("chatIdMessage").value;
  const message = document.getElementById("messageText").value;

  const response = await fetch(
    `${apiUrl}/waInstance${idInstance}/sendMessage/${apiTokenInstance}`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        chatId: chatId,
        message: message,
      }),
    }
  );

  const data = await response.json();

  showResponse(data);
}

async function sendFileByUrl() {
  const { idInstance, apiTokenInstance } = getCredentials();

  const chatId = document.getElementById("chatIdFile").value;
  const urlFile = document.getElementById("fileUrl").value;

  const response = await fetch(
    `${apiUrl}/waInstance${idInstance}/sendFileByUrl/${apiTokenInstance}`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },

  body: JSON.stringify({
    chatId: chatId,
    urlFile: urlFile,
    fileName: urlFile.split('/').pop().split('?')[0],
  }),
    }
  );

  const data = await response.json();

  showResponse(data);
}