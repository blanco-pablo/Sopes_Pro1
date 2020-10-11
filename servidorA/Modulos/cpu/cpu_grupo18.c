/*


Posterior a esto deberá listar todos los procesos, mostrando:

PID
Nombre
Estado



*/
#include <linux/module.h> 
#include <linux/kernel.h> 
#include <linux/init.h>
#include <linux/list.h>
#include <linux/types.h>
#include <linux/slab.h>
#include <linux/sched.h>
#include <linux/string.h>
#include <linux/fs.h>
#include <linux/seq_file.h>
#include <linux/proc_fs.h>
#include <asm/uaccess.h> 
#include <linux/hugetlb.h>
#include <linux/sched/signal.h>
#include <linux/sched.h>

#define FileProc "cpu_grupo18"
#define Carnet ""
#define Nombre "201504242"
#define Curso "Sistemas operativos 1"
#define SO "Ubuntu"

struct task_struct *task;
struct task_struct *task_child;
struct list_head *list;
s64 uptime;

static int proc_llenar_archivo(struct seq_file *m, void *v) {

    seq_printf(m, "[\n");
	
	int total = 0;
    int I= 0;
	int seg = 0;

	for_each_process(task){
		uptime = ktime_divns(ktime_get_boottime(), NSEC_PER_SEC);
		total = total + task->utime + task->stime;
		I = task->start_time;
		seg = seg + (uptime -(I / 100));

	}

	seq_printf(m, "%u\n",total);
	seq_printf(m, "%u\n",seg);
	seq_printf(m, "%u\n",(100 * ((total / 100 ) / seg ));
	return 0;
}



static int proc_al_abrir_archivo(struct inode *inode, struct  file *file) {
  return single_open(file, proc_llenar_archivo, NULL);
}

static struct file_operations myops =
{
        .owner = THIS_MODULE,
        .open = proc_al_abrir_archivo,
        .read = seq_read,
        .llseek = seq_lseek,
        .release = single_release,
};



static int simple_init(void){

    proc_create(FileProc,0,NULL,&myops);
    printk(KERN_INFO "Hola mundo - procesos %s\n", Nombre);
    return 0;
}

static void simple_clean(void){

    printk(KERN_INFO "“Sayonara mundo\n");
    remove_proc_entry(FileProc,NULL);
}



module_init(simple_init);
module_exit(simple_clean);
/*
 * Documentacion del modulo
 */
MODULE_LICENSE("GPL");
MODULE_AUTHOR(Nombre);
MODULE_DESCRIPTION("Modulo para mostrar info del estudiante y listar todos los procesos");
