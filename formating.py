import random

with open('extract_dialogues_from_anekdots.txt', encoding="utf8") as f:
    with open('train_anec.txt', 'w', encoding="utf8") as train_f:
        with open('valid_anec.txt', 'w', encoding="utf8") as val_f:
        
            anec_list = f.read().split('\n\n\n')
            for anec in anec_list:
            
                concat_line = anec.replace('\n- ', ' ')
                concat_line = "<s>" + concat_line[1:] + "</s>"
                
                if random.randint(1, 5) == 1:
                    val_f.write(concat_line + '\n')
                else:
                    train_f.write(concat_line + '\n')
                
                               
print('Done')
