import 'package:first_project/screens/important_tasks_screen.dart';
import 'package:first_project/screens/completed_tasks_screen.dart';
import 'package:first_project/screens/deleted_tasks_screen.dart';
import 'package:first_project/screens/pending_tasks_screen.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'models/task.dart';
import 'providers/task_provider.dart';
import 'screens/all_tasks_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Hive.initFlutter();

  Hive.registerAdapter(TaskAdapter());
  final taskBox = await Hive.openBox<Task>('tasks');
  final settingsBox = await Hive.openBox('settings');

  runApp(MyApp(
    taskBox: taskBox,
    settingsBox: settingsBox,
  ));
}

class MyApp extends StatefulWidget {
  final Box<Task> taskBox;
  final Box settingsBox;

  const MyApp({
    super.key,
    required this.taskBox,
    required this.settingsBox,
  });

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  bool isDarkMode = false;

  @override
  void initState() {
    super.initState();
    isDarkMode = widget.settingsBox.get('isDarkMode', defaultValue: false);
  }

  void toggleTheme() {
    setState(() {
      isDarkMode = !isDarkMode;
      widget.settingsBox.put('isDarkMode', isDarkMode); // Save preference
    });
  }

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(
          create: (_) =>
              TaskProvider(widget.taskBox), // Pass both boxes
        ),
      ],
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'ToDo App',
        theme: ThemeData.light(),
        darkTheme: ThemeData.dark(),
        themeMode: isDarkMode ? ThemeMode.dark : ThemeMode.light,
        initialRoute: '/',
        routes: {
          '/': (context) => HomeScreen(
                isDarkMode: isDarkMode,
                toggleTheme: toggleTheme,
              ),
          '/important': (context) => const ImportantTasksScreen(),
          '/Pending': (context) => const PendingTasksScreen(),
          '/completed': (context) => const CompletedTasksScreen(),
          '/deleted': (context) => const DeletedTasksScreen(),
        },
      ),
    );
  }
}
