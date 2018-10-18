import React, { Component } from 'react';
import './Login.css';
import {Container, Row, Col, Button, Form, FormGroup, Label, Input } from 'reactstrap';

class Login extends Component {
  render() {
    return (
      <Container className="container">
      <Row className="logo">
      <Col md={12} className="logo-text">
      <h1>Budzet Domowy</h1>
      </Col>
      </Row>
      <Row className="content">
      <div className="login">
      <Form>
      <FormGroup row>
          <Label for="exampleEmail" sm={2}>Email</Label>
          <Col sm={10}>
            <Input type="email" name="email" id="exampleEmail" placeholder="something@idk.cool" />
          </Col>
        </FormGroup>
        <FormGroup row>
          <Label for="examplePassword" sm={2}>Password</Label>
          <Col sm={10}>
            <Input type="password" name="password" />
          </Col>
        </FormGroup>
        <FormGroup check row>
          <Col sm={12}>
            <Button>Log in</Button>
          </Col>
        </FormGroup>
      </Form>
      </div>
      </Row>
      <Row>
      <Col xs="12" >
      footer     
      </Col>
      </Row>
      </Container>
    );
  }
}

export default Login;