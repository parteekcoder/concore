import github
from github import Github
<<<<<<< Updated upstream
import os,sys,time,platform,base64
=======
import os,sys,platform,base64,time,requests,json
>>>>>>> Stashed changes

# Intializing the Variables
# Hashed token
BOT_TOKEN = 'Z2l0aHViX3BhdF8xMUFYS0pGVFkwd2xwT0dmYldFOTBBXzN3Nkx2THpiaUFKek5pTDdqNlpLUzVwUUpoTlJWR3dtNnM0NWNDa0RmWTJaTTZLSUpHRHhERlhrZlJS'
BOT_REPO_NAME = 'concore-studies-staging'        #bot repo name
UPSTREAM_REPO_NAME = 'concore-studies'        #bot repo name
OWNER_NAME = 'ControlCore-Project'  #account name
STUDY_NAME =  sys.argv[1]
STUDY_NAME_PATH =  sys.argv[2]
AUTHOR_NAME =  sys.argv[3]
BRANCH_NAME =  sys.argv[4]
PR_TITLE =  sys.argv[5]
PR_BODY =  sys.argv[6]

# Defining Functions
def checkInputValidity():
    if AUTHOR_NAME=="" or STUDY_NAME=="" or STUDY_NAME=="":
        print("Please Provide necessary Inputs")
        exit(0)
    if not os.path.isdir(STUDY_NAME_PATH):
        print("Directory doesnot Exists.Invalid Path")
        exit(0)


def getPRs(upstream_repo):
    try:
<<<<<<< Updated upstream
        return upstream_repo.get_pulls(head=f'{OWNER_NAME}:{BRANCH_NAME}')
    except Exception as e:
=======
        return upstream_repo.get_pulls(head=f'{BOT_ACCOUNT}:{BRANCH_NAME}')
    except:
>>>>>>> Stashed changes
        print("Not able to fetch Status of your example.Please try after some time.")
        exit(0)

def printPR(pr):
    print(f'Check your example here https://github.com/{OWNER_NAME}/{UPSTREAM_REPO_NAME}/pulls/'+str(pr.number),end="")

def anyOpenPR(upstream_repo):
    pr = getPRs(upstream_repo)
    openPr=None
    for i in pr:
        if i.state=="open":
            openPr=i
            break
    return openPr

def commitAndUpdateRef(repo,tree_content,commit,branch):
    try:
        print(time.time())
        new_tree = requests.post(url=f"https://api.github.com/repos/{BOT_ACCOUNT}/{REPO_NAME}/git/trees",data=json.dumps({'base_tree':commit.commit.tree.sha,'tree':tree_content}),headers={'Authorization':'Bearer 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'}).json()
        new_commit = requests.post(url=f"https://api.github.com/repos/{BOT_ACCOUNT}/{REPO_NAME}/git/commits",data=json.dumps({'message':'commit message','tree':new_tree['sha'],'parents':[commit.commit.sha]}),headers={'Authorization':'Bearer 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'}).json()
        # new_tree = repo.create_git_tree(tree=tree_content,base_tree=commit.commit.tree)
        # new_commit = repo.create_git_commit("commit message",new_tree,[commit.commit])
        print(time.time())
        if len(repo.compare(base=commit.commit.sha,head=new_commit['sha']).files) == 0:
            print("Your don't have any new changes.May be your example is already accepted.If this is not the case try with different fields.")
            exit(0)
        ref = repo.get_git_ref("heads/"+branch.name)
        ref.edit(new_commit['sha'],True)
    except Exception as e:
        print("failed to Upload your example.Please try after some time.",end="")
        exit(0)


def appendBlobInTree(repo,content,file_path,tree_content):
    blob = repo.create_git_blob(content,'utf-8')
    tree_content.append( {'path':file_path,'mode':"100644",'type':"blob",'sha':blob.sha})


def runWorkflow(repo,upstream_repo):
    openPR = anyOpenPR(upstream_repo)
    if openPR==None:
        workflow_runned = repo.get_workflow(id_or_name="pull_request.yml").create_dispatch(ref=BRANCH_NAME,inputs={'title':PR_TITLE,'body':PR_BODY,'upstreamRepo':UPSTREAM_REPO_NAME,'account':OWNER_NAME})
        if not workflow_runned:
            print("Some error occured.Please try after some time")
            exit(0)
        else:
            printPRStatus(upstream_repo)
    else:
        print("Successfully uploaded all files,your example is in waiting.Please wait for us to accept it.",end="")
        printPR(openPR)

def printPRStatus(upstream_repo):
    try:
<<<<<<< Updated upstream
        time.sleep(15)
        openPR = anyOpenPR(upstream_repo)
        if openPR==None:
            print("Someting went wrong or your example already exist.If this is not the case try with different fields")
            exit(0)
        printPR(openPR)
    except Exception as e:
=======
        issues = upstream_repo.get_issues()
        pulls = upstream_repo.get_pulls(state='all')
        max_num = -1
        for i in issues:
            max_num = max(max_num,i.number)
        for i in pulls:
            max_num = max(max_num,i.number)
        print(f'Check your example here https://github.com/{UPSTREAM_ACCOUNT}/{REPO_NAME}/pulls/{max_num+1}',end="")
    except:
>>>>>>> Stashed changes
        print("Your example successfully uploaded but unable to fetch status.Please try again")
    

def isImageFile(filename):
    image_extensions = ['.jpeg', '.jpg', '.png']
    _, file_extension = os.path.splitext(filename)
    return file_extension.lower() in image_extensions


# Decode Github Token
def decode_token(encoded_token):
    decoded_bytes = base64.b64decode(encoded_token.encode('utf-8'))
    decoded_token = decoded_bytes.decode('utf-8')
    return decoded_token


# check if directory path is Valid
checkInputValidity()


# Authenticating Github with Access token
try:
    if BRANCH_NAME=="#":
        BRANCH_NAME=AUTHOR_NAME+"_"+STUDY_NAME
    if PR_TITLE=="#":
        PR_TITLE=f"Contributing Study {STUDY_NAME} by {AUTHOR_NAME}"
    if PR_BODY=="#":
        PR_BODY=f"Study Name: {STUDY_NAME} \n Author Name: {AUTHOR_NAME}"
<<<<<<< Updated upstream
    AUTHOR_NAME = AUTHOR_NAME.replace(" ","_")
    DIR_PATH = AUTHOR_NAME + '_' + STUDY_NAME
    g = Github(decode_token(BOT_TOKEN))
    repo = g.get_user(OWNER_NAME).get_repo(BOT_REPO_NAME)
    upstream_repo = g.get_repo(f'{OWNER_NAME}/{UPSTREAM_REPO_NAME}') #controlcore-Project/concore
=======
    DIR_PATH = STUDY_NAME
    g = Github(decode_token(BOT_TOKEN))
    repo = g.get_repo(f"{BOT_ACCOUNT}/{REPO_NAME}")
    upstream_repo = g.get_repo(f'{UPSTREAM_ACCOUNT}/{REPO_NAME}') #controlcore-Project/concore-studies
>>>>>>> Stashed changes
    base_ref = upstream_repo.get_branch(repo.default_branch)
    AUTHOR_NAME = AUTHOR_NAME.replace(" ","_")
    BRANCH_NAME = BRANCH_NAME.replace(" ","_")
    DIR_PATH = DIR_PATH.replace(" ","_")
<<<<<<< Updated upstream
    is_present = any(branch.name == BRANCH_NAME for branch in branches)
except:
    print("Some error occured.Authentication failed",end="")
    exit(0)
=======
    is_present = False
    branch = repo.get_branch(BRANCH_NAME)
    is_present=True
except:
    print("Creating new example study.",end="")
>>>>>>> Stashed changes



# If creating PR First Time
# Create New Branch for that exmaple
if not is_present:
    repo.create_git_ref(f'refs/heads/{BRANCH_NAME}', base_ref.commit.sha)
    branch = repo.get_branch(branch=BRANCH_NAME)


tree_content = []

try:
    for root, dirs, files in os.walk(STUDY_NAME_PATH):
        for filename in files:
            path = os.path.join(root, filename)
            if isImageFile(filename):
                with open(path, 'rb') as file:
                    image = file.read()
                    content = base64.b64encode(image).decode('utf-8')
            else:
                with open(path, 'r') as file:
                    content = file.read()
            file_path = f'{DIR_PATH+path.removeprefix(STUDY_NAME_PATH)}'
            if(platform.uname()[0]=='Windows'): file_path=file_path.replace("\\","/")
            appendBlobInTree(repo,content,file_path,tree_content)
    print(f"Commit start {time.time()}")
    commitAndUpdateRef(repo,tree_content,base_ref.commit,branch)
    print(f"workflow start {time.time()}")
    runWorkflow(repo,upstream_repo)
except:
    print("Some error Occured.Please try again after some time.",end="")
    exit(0)