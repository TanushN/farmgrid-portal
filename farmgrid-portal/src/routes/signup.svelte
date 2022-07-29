<script>
  import { user } from "../stores";
  import { navigate } from "svelte-navigator";
  import {
    TextInput,
    PasswordInput,
    Button,
    ToastNotification,
  } from "carbon-components-svelte";
  import Api from "../util/api";

  async function signup() {
    
    try {
      const response = await Api.post("/auth/signup", {
        email: email,
        password: password,
      });

      console.log("Signed up!");

      showToast = true;
      toastSubtitle = "Successfully signed up! Please login below.";
      toastType = "success";

    
      navigate("/login", { replace: true });
    } catch (error) {
      console.error(error);
      showToast = true;
      toastSubtitle = error.response.data.detail;
      toastType = "error";
    }
  }

  let email;
  let password;

  let showToast = false;
  let toastSubtitle;
  let toastType;
</script>

<main>
  <div class="signup">
    <h3>Sign Up</h3>
    <TextInput
      bind:value={email}
      labelText="Email"
      placeholder="example@gmail.com"
    />
    <PasswordInput
      bind:value={password}
      labelText="Password"
      placeholder="Enter password..."
    />
    <div width="fit-content">
      <Button on:click={signup}>Sign Up</Button>
    </div>
    <a href="login">Already have an account? Login here instead.</a>
  </div>
  {#if showToast}
    <ToastNotification
      lowContrast
      kind={toastType}
      title={toastType}
      subtitle={toastSubtitle}
      caption={new Date().toLocaleString()}
      on:close={() => (showToast = false)}
    />
  {/if}
</main>

<style>
  .signup {
    display: flex;
    position: absolute;
    row-gap: 1rem;
    flex-direction: column;
    width: 27rem;
    justify-content: flex-start;
    width: 20%;
    top: 40%;
    left: 40%;
    right: 40%;
  }
</style>
