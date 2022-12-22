import 'package:flutter/material.dart';

class LearnFlutterPage extends StatefulWidget {
  const LearnFlutterPage({super.key});

  @override
  State<LearnFlutterPage> createState() => _LearnFlutterPageState();
}

class _LearnFlutterPageState extends State<LearnFlutterPage> {
  bool isSwitched = false;
  bool? isCheckbox = false;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('Learn Flutter'),
          automaticallyImplyLeading: false,
          leading: IconButton(
            icon: const Icon(Icons.arrow_back_ios_new),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
          actions: [
            IconButton(
              onPressed: () {
                debugPrint('Actions');
              },
              icon: const Icon(
                Icons.info_outline,
              ),
            )
          ],
        ),
        body: SingleChildScrollView(
          child: Column(
            children: [
              Image.asset('images/meme.jpg', width: 300, height: 300),
              const SizedBox(height: 10),
              const Divider(
                color: Colors.black,
              ),
              Container(
                margin: const EdgeInsets.all(10),
                padding: const EdgeInsets.all(10),
                color: Colors.blueGrey,
                child: const Center(
                  child: Text(
                    'This is a meme',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 20,
                    ),
                  ),
                ),
              ),
              ElevatedButton(
                style: ElevatedButton.styleFrom(
                  backgroundColor: isSwitched ? Colors.green : Colors.red,
                ),
                onPressed: () {
                  debugPrint('Elevated Button pressed');
                },
                child: const Text('Elevated Button'),
              ),
              OutlinedButton(
                onPressed: () {
                  debugPrint('Outlined Button pressed');
                },
                child: const Text('Outlined Button'),
              ),
              TextButton(
                onPressed: () {
                  debugPrint('Text Button pressed');
                },
                child: const Text('Text Button'),
              ),
              GestureDetector(
                behavior: HitTestBehavior.opaque,
                onTap: () {
                  debugPrint('This is the Row Widget');
                },
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: const [
                    Icon(
                      Icons.local_fire_department,
                      color: Colors.red,
                    ),
                    Text('Row Widget'),
                    Icon(
                      Icons.local_fire_department,
                      color: Colors.red,
                    ),
                  ],
                ),
              ),
              Switch(
                  value: isSwitched,
                  onChanged: (bool newBool) {
                    setState(() {
                      isSwitched = newBool;
                    });
                  }),
              Checkbox(
                  value: isCheckbox,
                  onChanged: (bool? newBool) {
                    setState(() {
                      isCheckbox = newBool;
                    });
                  }),
              Image.network('https://picsum.photos/250?image=9'),
            ],
          ),
        ));
  }
}
