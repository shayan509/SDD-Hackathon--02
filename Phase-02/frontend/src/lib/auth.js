const TOKEN_KEY = "access_token";

function decodeJwtPayload(token) {
  try {
    const payload = token.split(".")[1];
    return JSON.parse(atob(payload));
  } catch {
    return null;
  }
}

export function getToken() {
  if (typeof window === "undefined") {
    return null;
  }
  const token = localStorage.getItem(TOKEN_KEY);
  if (!token) {
    return null;
  }
  const payload = decodeJwtPayload(token);
  if (payload?.exp && Date.now() >= payload.exp * 1000) {
    localStorage.removeItem(TOKEN_KEY);
    return null;
  }
  return token;
}

export function setToken(token) {
  if (typeof window === "undefined") {
    return;
  }
  localStorage.setItem(TOKEN_KEY, token);
}

export function clearToken() {
  if (typeof window === "undefined") {
    return;
  }
  localStorage.removeItem(TOKEN_KEY);
}

export function isAuthenticated() {
  return Boolean(getToken());
}
