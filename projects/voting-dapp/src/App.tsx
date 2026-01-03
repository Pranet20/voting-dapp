import { useEffect, useState } from "react";
import algosdk from "algosdk";

const algod = new algosdk.Algodv2(
  "",
  "https://testnet-api.algonode.cloud",
  ""
);

function App() {
  const [status, setStatus] = useState("Connecting...");

  useEffect(() => {
    algod.status().do()
      .then(() => setStatus("Connected to Algorand TestNet ✅"))
      .catch(() => setStatus("Connection failed ❌"));
  }, []);

  return (
    <div style={{ padding: "40px" }}>
      <h1>Voting dApp</h1>
      <p>App ID: <b>753090022</b></p>
      <p>Status: {status}</p>
    </div>
  );
}

export default App;