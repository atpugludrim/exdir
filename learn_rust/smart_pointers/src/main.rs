use std::cell::RefCell;
use std::rc::Rc;
#[derive(Debug)]
struct TreeNode {
    val: i32,
    left: Option<Rc<RefCell<TreeNode>>>,
    right: Option<Rc<RefCell<TreeNode>>>
}
impl TreeNode {
    fn new(val: i32) -> Self {
        Self {
            val,
            left: None,
            right: None
        }
    }
}
fn main() {
    let rcp : Rc<i32> = Rc::new(5);
    let rfcp : RefCell<i32> = RefCell::new(3);
    println!("{}", *rcp);
    println!("{}", *rfcp.borrow());
    *rfcp.borrow_mut() += 1;
    println!("{}", *rfcp.borrow());
    let p: Rc<RefCell<i32>> = Rc::new(RefCell::new(2));
    let q = Rc::clone(&p);
    println!("{}", *p.borrow());
    *q.borrow_mut() += 1;
    println!("{}", *q.borrow());
    //
    let root = Rc::new(RefCell::new(TreeNode::new(5)));
    println!("{:?}", root);
    let left = Some(Rc::new(RefCell::new(TreeNode::new(6))));
    root.borrow_mut().left = left;
    println!("{:?}", root);
    let right = Some(Rc::new(RefCell::new(TreeNode::new(7))));
    root.borrow_mut().right = right;
    println!("{:?}", root);
    println!("{}", root.borrow().val);
}
