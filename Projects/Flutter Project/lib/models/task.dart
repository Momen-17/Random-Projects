import 'package:hive/hive.dart';

part 'task.g.dart';

@HiveType(typeId: 0)
class Task extends HiveObject {
  @HiveField(0)
  final String id;

  @HiveField(1)
  final String title;

  @HiveField(2)
  final bool isCompleted;

  @HiveField(3)
  final bool isImportant;

  @HiveField(4)
  final bool isDeleted;

  Task({
    required this.id,
    required this.title,
    this.isCompleted = false,
    this.isImportant = false,
    this.isDeleted = false,
  });

  Task copyWith({String? title, bool? isCompleted, bool? isImportant, bool? isDeleted}) {
    return Task(
      id: id,
      title: title ?? this.title,
      isCompleted: isCompleted ?? this.isCompleted,
      isImportant: isImportant ?? this.isImportant,
      isDeleted: isDeleted ?? this.isDeleted,
    );
  }
}
