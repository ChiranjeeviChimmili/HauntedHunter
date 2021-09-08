import "./App.css";
import Button from "react-bootstrap/Button";
import "bootstrap/dist/css/bootstrap.min.css";
import React, { useState, useEffect } from "react";
import axios from "axios";
import { Formik, Form, Field } from "formik";

function App() {
  const [isLoading, setLoading] = useState(false);

  const handleClick = () => setLoading(true);

  return (
    <div className="App">
      <Formik
        initialValues={{
          city: "",
          state: "",
        }}
        onSubmit={async (values) => {
          console.log(values.city, values.state);
          if(!isLoading) handleClick();
          await networkDoubler(values.city, values.state);
          setLoading(false);
        }}
      >
        <Form>
          <Field id="city" name="city" placeholder="Atlanta" />

          <Field id="state" name="state" placeholder="Georgia" />

          <Button disabled={isLoading} type="submit">
            {isLoading ? "Loading…" : "Submit"}
          </Button>
        </Form>
      </Formik>
    </div>
  );
}

async function networkDoubler(city, state) {
  axios
    .post("/", {
      city: city,
      state: state,
    })
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
}

export default App;
