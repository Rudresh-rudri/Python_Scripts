#student_marks = 36

#if student_marks > 35:
 #   print("congrats you are passed")
#if student_marks > 85:
 #   print("distinction")
#if student_marks > 75 :
 #   print("firstclass")
#if student_marks !=35 :
#      print("failed")
################################################
######name validation logic################
##############################################



#name = 'rueeeeeeeeee'
#if len(name)<3:
#    print("name is very short:")
#elif  len(name)>12:
#    print("name is very long:")
#else:
#    print('name validated:')
###################################################################
#mobile_storage = 1

#if mobile_storage <10:
# 3   print("please charge yourphone")
 # print("power saving mode on")
#elif mobile_storage == 100:
#    print("power saving mode off and barety about to full")
#else:
#    print("normal")
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[
#
#######################################################################################
##########   distence converter     ################################
##########################################################################################
distance= int(input('please enter the distence travelled:'))
unit = input('INPUT TYPE is k for kms or m for miles:')
if unit.lower() =='k':
    converted= distance/1.609
    print(f"you have travelled {converted}'miles")

elif unit.upper() == 'M':
    converted = distance*1.609
    print(f"you have covered {converted}kms:")
#else:
 #   print("wrong input")

    ####################################


