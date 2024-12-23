import 'package:flutter/material.dart';

class DrawerMenu extends StatelessWidget {
  const DrawerMenu({super.key});

  @override
  Widget build(BuildContext context) {
    final isDarkMode = Theme.of(context).brightness == Brightness.dark;

    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: [
          Container(
            height: 80,
            color: isDarkMode ? const Color.fromARGB(255, 145, 103, 242) : Theme.of(context).primaryColor,
            padding: const EdgeInsets.symmetric(horizontal: 16.0),
            alignment: Alignment.centerLeft,
            child: const Text(
              'Menu',
              style: TextStyle(
                color: Colors.white,
                fontSize: 24,
              ),
            ),
          ),
          ListTile(
            leading: const Icon(Icons.list),
            title: const Text('All Tasks'),
            onTap: () {
              Navigator.pop(context); // Close drawer
              Navigator.pushReplacementNamed(context, '/');
            },
          ),
          ListTile(
            leading: const Icon(Icons.star, color: Colors.blue),
            title: const Text('Important'),
            onTap: () {
              Navigator.pop(context); // Close drawer
              Navigator.pushNamed(context, '/important');
            },
          ),
          ListTile(
            leading: const Icon(Icons.check_box_outline_blank_sharp, color: Colors.orange,),
            title: const Text('Pending'),
            onTap: () {
              Navigator.pop(context);
              Navigator.pushNamed(context, '/Pending');
            },
          ),
          ListTile(
            leading: const Icon(Icons.check_box_outlined, color: Colors.green,),
            title: const Text('Completed'),
            onTap: () {
              Navigator.pop(context);
              Navigator.pushNamed(context, '/completed');
            },
          ),
          ListTile(
            leading: const Icon(Icons.delete, color: Colors.red,),
            title: const Text('Deleted'),
            onTap: () {
              Navigator.pop(context);
              Navigator.pushNamed(context, '/deleted');
            },
          ),
        ],
      ),
    );
  }
}
