import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Dream UI',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Welcome to My Dream App!'),
        backgroundColor: Colors.orangeAccent,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            // Text widget to greet the user
            Text(
              'Hello, Flutter World! 🌎',
              style: TextStyle(
                fontSize: 30,
                fontWeight: FontWeight.bold,
                color: Colors.blueAccent,
              ),
            ),
            SizedBox(height: 20),

            // Elevated Button to print message on click
            ElevatedButton(
              onPressed: () {
                print('ElevatedButton Clicked!');
              },
              style: ElevatedButton.styleFrom(
                primary: Colors.green, // background color
                onPrimary: Colors.white, // text color
              ),
              child: Text('Click Me!'),
            ),
            SizedBox(height: 20),

            // Image from the internet
            Image.network(
              'https://flutter.dev/assets/flutter-logo-sharing-8d0b6a39284bc1b4d23135a458b7a66fd5997dbdc440fd8e404b5c78b9c06e53.png',
              height: 100,
            ),
          ],
        ),
      ),
    );
  }
}
